"""Check material integrity and safety boundaries, not model performance."""
from pathlib import Path
import ast
import hashlib
import json
import tempfile
import unittest
from evidence_state_repro.replay import verify_manifest, load_rows
from evidence_state_repro.offline import ranking, safe_output
ROOT=Path(__file__).resolve().parents[1]

class ReleaseContracts(unittest.TestCase):
    def test_manifest(self):self.assertGreater(verify_manifest(ROOT),30)
    def test_scalar_scoring_function_bodies(self):
        for entry in json.loads((ROOT/'provenance/computation_kernels.json').read_text('utf-8')):
            text=(ROOT/entry['candidate_path']).read_text('utf-8')
            funcs={n.name:n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef)}
            for f in entry['unchanged_functions']:
                self.assertEqual(hashlib.sha256(ast.get_source_segment(text,funcs[f['name']]).encode()).hexdigest(),f['body_sha256'])
    def test_no_reference_fields_in_prediction_projections(self):
        for p in (ROOT/'frozen_results/predictions').glob('*.jsonl'):
            for r in load_rows(p):self.assertEqual(set(r),{'qid','methods'})
    def test_all_mapping_paths_exist(self):
        mapping=json.loads((ROOT/'provenance/table_mapping.json').read_text('utf-8'))
        self.assertEqual(len(mapping),26)
        for row in mapping:
            for name in row['files']:self.assertTrue((ROOT/name).is_file(),name)
    def test_table_formula_reference_counts(self):
        self.assertEqual(len(json.loads((ROOT/'frozen_results/metrics/manuscript_tables.json').read_text('utf-8'))),26)
        self.assertEqual(len(json.loads((ROOT/'configs/equation_contracts.json').read_text('utf-8'))),13)
        self.assertEqual(len(json.loads((ROOT/'docs/references.json').read_text('utf-8'))),34)
    def test_forced_minicheck_scores_inapplicable(self):
        rows=load_rows(ROOT/'external_comparisons/locked1341.jsonl')
        for m in ['MiniCheck-only','G12+MiniCheck-LR']:
            forced=[r['methods'][m] for r in rows if r['methods'][m]['forced']]
            self.assertEqual(len(forced),6)
            self.assertTrue(all(r['risk'] is None for r in forced))
    def test_tied_AP_AUC(self):
        r=[{'qid':q,'initial_wrong_label':y,'scores':{'X':s},'saved_selected':{'X':q=='a'}}
           for q,y,s in [('a',1,.9),('b',0,.9),('c',1,.2),('d',0,.0)]]
        x=ranking(r,'X');self.assertAlmostEqual(x['AP_percent'],(1/4+1/3)*100);self.assertAlmostEqual(x['ROC_AUC_percent'],62.5)
    def test_repository_output_guard(self):
        with self.assertRaises(ValueError):safe_output(ROOT,ROOT/'references')
    def test_recorded_random_memberships(self):
        rows=load_rows(ROOT/'frozen_results/selections/locked1341_random_five_assignments.jsonl')
        scores={r['qid']:r for r in load_rows(ROOT/'frozen_results/metrics/locked1341.jsonl')}
        self.assertEqual(len(rows),1341)
        for m,overlap in zip(rows[0]['selected'],[1,2,2,0,1]):
            self.assertEqual(sum(r['selected'][m] for r in rows),269)
            self.assertEqual(sum(r['b3_forced_reference'] and r['selected'][m] for r in rows),overlap)
            for r in rows:
                if not r['selected'][m]:self.assertEqual(scores[r['qid']]['methods'][m],scores[r['qid']]['methods']['Initial'])
        rows=load_rows(ROOT/'frozen_results/selections/m3vqa_random20_selection.jsonl')
        self.assertEqual(len(rows),13125);self.assertEqual(sum(r['selected'] for r in rows),2625)
        self.assertEqual(sum(r['forced'] and r['selected'] for r in rows),515)

if __name__=='__main__':unittest.main()
