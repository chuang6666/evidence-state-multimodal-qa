"""Join existing frozen aggregators into the current manuscript table numbering."""
import importlib.util
import json
from pathlib import Path
from .offline import main_tables, safe_output, csv_table, dump

def run(root,output):
    root=Path(root).resolve()
    base=main_tables(root,output)
    module_path=root/'external_comparisons/replay.py'
    spec=importlib.util.spec_from_file_location('ijmlc_external_replay',module_path)
    ext=importlib.util.module_from_spec(spec);spec.loader.exec_module(ext)
    dev=ext.read_index(root/'external_comparisons/dev1096.jsonl')
    locked=ext.read_index(root/'external_comparisons/locked1341.jsonl')
    formal=ext.read_index(root/'frozen_results/rankings/dev1096_oof.jsonl')
    expectations=json.loads((root/'external_comparisons/expected.json').read_text('utf-8'))
    external_dev=[];external_end=[];external_decomp=[]
    for method,v in expectations.items():
        external_dev.append(ext.dev_summary(dev,formal,method,v['dev']))
        d=ext.locked_summary(locked,method,v['locked'],False)
        name=method+'-20'
        external_end.append({'method':name,'selected':269,'em_percent':d['em']*100,'token_f1_percent':d['f1']*100,
            'W2R':d['wrong_to_right'],'R2W':d['right_to_wrong'],'Net':d['net']})
        external_decomp.append({'method':name,'selected':269,'selected_wrong':d['selected_initial_errors'],
            'error_rate_percent':d['selected_initial_errors']/269*100,'W2R':d['wrong_to_right'],'repair_yield_percent':d['repair_yield']*100})
    tables=base['tables']
    tables['Table3_external_risk_signals']=[d for d in tables['Table2_formal_oof'] if d['variant'] in ['G0','CLEAN_B3']]+external_dev
    saved=tables['Table4_mmqa_base_endpoints']
    tables['Table4_locked1341_ten_configurations']=[d for d in saved if not d['method'].startswith('Random-')]+external_end
    random=tables['Table4_random_mean_sample_SD']
    tables['Table4_locked1341_ten_configurations'].append({'method':'Random-20','selected':269,
        **{v['metric']:v['mean'] for v in random},'sample_SD':{v['metric']:v['sample_SD'] for v in random}})
    assert len(tables['Table4_locked1341_ten_configurations'])==10
    tables['Table5_selected_error_and_repair_yield']+=external_decomp
    case=json.loads((root/'frozen_results/metrics/qualitative_case_qid_map.json').read_text('utf-8'))
    tables['Table9_case_QID_transitions']=case['cases']
    for name,rows in tables.items():csv_table(Path(output)/(name+'.csv'),rows)
    result={'status':'PASS_IJMLC_TABLES_FROM_FROZEN_RECORDS','tables':tables,
        'scope':'Numeric main tables 2–8 and Table 9 QID/transition mapping; SI/specification records are mapped separately.',
        'output_pool_note':'The four later external adaptations share legal outputs for shared selections. Original B3/G0 outputs remain separately frozen; cross-strategy pairing does not isolate a pure selector effect.'}
    dump(Path(output)/'ijmlc_tables.json',result)
    return result
