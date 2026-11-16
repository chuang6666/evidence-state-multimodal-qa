"""Replay saved structural comparisons; optionally rerun their fixed-score bootstrap."""
import json
from pathlib import Path
import statistics
import numpy as np
from .replay import load_rows, assert_close, verify_manifest
from .offline import dump, safe_output
from .structural_kernels import metrics

def run(root,output=None,bootstrap=False):
    root=Path(root).resolve();verify_manifest(root)
    expected=json.loads((root/'frozen_results/metrics/structural_increment_expected.json').read_text('utf-8'))
    formal={r['qid']:r for r in load_rows(root/'frozen_results/rankings/dev1096_oof.jsonl')}
    explanatory={r['qid']:r for r in load_rows(root/'frozen_results/rankings/dev1096_explanatory_oof.jsonl')}
    qids=sorted(formal);assert len(qids)==1096 and set(formal)==set(explanatory)
    y=np.array([formal[q]['initial_wrong_label'] for q in qids]);qr=np.arange(1096)
    assert y.sum()==680
    scores={m:np.array([(explanatory[q] if m in ['A4','A6'] else formal[q])['scores'][m if m in ['A4','A6','G0'] else 'CLEAN_'+m] for q in qids]) for m in ['A4','A6','B3','B2','G0']}
    assert np.array_equal(scores['A6'],scores['B3'])
    orders={m:np.lexsort((qr,-s)) for m,s in scores.items()}
    selected={m:{qids[int(i)] for i in ix[:220]} for m,ix in orders.items()}
    ranks={m:{qids[int(v)]:i+1 for i,v in enumerate(ix)} for m,ix in orders.items()}
    def desc(qs):
        wrong=sum(formal[q]['initial_wrong_label'] for q in qs)
        return {'N':len(qs),'initial_wrong':wrong,'initial_correct':len(qs)-wrong,'qids':sorted(qs)}
    groups={'shared':desc(selected['A4']&selected['B3']),'B3_only':desc(selected['B3']-selected['A4']),
            'A4_only':desc(selected['A4']-selected['B3']),'neither':desc(set(qids)-selected['A4']-selected['B3'])}
    assert groups==expected['selected']
    movement=np.array([ranks['A4'][q]-ranks['B3'][q] for q in qids])
    ranking={'spearman':float(np.corrcoef([ranks['A4'][q] for q in qids],[ranks['B3'][q] for q in qids])[0,1]),
       'moved_up':int((movement>0).sum()),'moved_down':int((movement<0).sum()),'same_rank':int((movement==0).sum()),
       'median_absolute_move':float(np.median(np.abs(movement))),'max_absolute_move':int(np.abs(movement).max())}
    assert_close(ranking,{k:expected['ranking'][k] for k in ranking},'ranking',1e-12)
    b2={'shared_top220':desc(selected['B2']&selected['B3']),'B2_only':desc(selected['B2']-selected['B3']),
        'B3_only':desc(selected['B3']-selected['B2'])}
    assert_close(b2,{k:expected['B2_B3'][k] for k in b2},'B2_B3',1e-12)
    metric_names=['precision_at_220','recall_at_220','AP','AUC']
    points={m:dict(zip(metric_names,metrics(y,s,qr).tolist())) for m,s in scores.items()}
    assert_close(points,expected['method_metrics'],'structural points',1e-12)
    controlled={r['qid']:r for r in load_rows(root/'frozen_results/metrics/dev1096_controlled.jsonl')}
    assert all(controlled[q]['methods']['A4']==controlled[q]['methods']['A6'] for q in groups['shared']['qids'])
    def transitions(qs,m):
        return {'N':len(qs),'initial_wrong':desc(qs)['initial_wrong'],
          'W2R':sum(controlled[q]['methods']['Initial']['em']==0 and controlled[q]['methods'][m]['em']==1 for q in qs),
          'R2W':sum(controlled[q]['methods']['Initial']['em']==1 and controlled[q]['methods'][m]['em']==0 for q in qs)}
    assert transitions(groups['B3_only']['qids'],'A6')==expected['controlled_B3_only']
    assert transitions(groups['A4_only']['qids'],'A4')==expected['controlled_A4_only']
    result={'status':'PASS_FIXED_SCORE_STRUCTURAL_COMPARISON','selected_counts':{k:{n:v for n,v in d.items() if n!='qids'} for k,d in groups.items()},
        'B2_B3':{k:{n:v for n,v in d.items() if n!='qids'} for k,d in b2.items()},'ranking':ranking,'points':points,
        'scope':'Fixed OOF predictions only; no fitting, extraction, generation, or model selection.', 'model_fits':0}
    if bootstrap:
        # Same seed, QID order, sample multiplicity and numerical kernels as the saved analysis.
        cfg=expected['scope'];rng=np.random.default_rng(cfg['paired_bootstrap_seed'])
        reps=np.empty((cfg['replicates'],4))
        for k in range(cfg['replicates']):
            sample=rng.integers(0,1096,size=1096)
            assert len(np.unique(y[sample]))==2
            reps[k]=metrics(y[sample],scores['B3'][sample],qr[sample])-metrics(y[sample],scores['A4'][sample],qr[sample])
        observed=metrics(y,scores['B3'],qr)-metrics(y,scores['A4'],qr)
        computed={n:{'B3_minus_A4':float(observed[i]),'percentile95_CI':np.percentile(reps[:,i],[2.5,97.5]).tolist(),
           'fraction_gt_zero':float((reps[:,i]>0).mean()),'fraction_eq_zero':float((reps[:,i]==0).mean())}
           for i,n in enumerate(['P_at_220','R_at_220','AP','AUC'])}
        assert_close(computed,expected['fixed_score_paired_bootstrap'],'structural fixed-score bootstrap',1e-12)
        result['fixed_score_paired_bootstrap']=computed
    if output:
        dest=safe_output(root,output);dump(dest/'structural_comparison.json',result)
    return result
