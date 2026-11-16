# Reproduction guide

Run the environment installation and core commands in the root README from a fresh checkout. `requirements.txt` pins NumPy 2.3.5 for the saved statistical protocols; ordinary ranking/endpoint aggregation uses the standard library. Installing the package requires the standard setuptools build backend. No inference library or credentials are required.

## Commands and outputs

1. `python -m evidence_state_repro verify`: SHA-256 verification of the listed immutable payload.
2. `python -m evidence_state_repro replay`: original numeric score, Top-220, forced membership, locked endpoint, Random summary and transfer checks.
3. `python -m evidence_state_repro tables --output-dir ../ijmlc-tables`: current main-table CSVs, including all ten locked configurations and six external-risk rows. Individual five-seed records accompany the Random-20 summary.
4. `python external_comparisons/replay.py`: frozen direct/external-LR risk rankings and 269-case endpoints.
5. `python -m evidence_state_repro structural`: A4/B3 and B2/B3 selection differences, actual rank movement, AP/AUC and controlled exclusive-case outcomes.
6. `python -m evidence_state_repro statistics --output-dir ../ijmlc-statistics`: 24 specified endpoint/component confidence-interval checks and associated tests, following saved order/seeds.
7. `python external_comparisons/replay.py --statistics`: paired external-versus-B3 EM/F1 intervals and exact McNemar checks.
8. `python -m evidence_state_repro structural-statistics --output-dir ../ijmlc-structural-statistics`: the already-defined four-metric A4/B3 fixed-score bootstrap, seed 260817, 10,000 resamples of 1,096 QIDs. This does not assess model-retraining stability or reselect B3.

Every output location must be outside the repository and new/empty. Keep generated references and result directories outside Git. The checked module location must point to the fresh checkout's `src/evidence_state_repro`, not a research workstation path.

## Optional frozen-answer rescoring

Obtain the original provider files under their access terms. The following commands do not download data or call models:

```bash
python -m evidence_state_repro prepare-references --mmqa-data /provider/MMQA_dev.jsonl.gz --m3-data /provider/quesions.jsonl --output-dir ../local-references
python -m evidence_state_repro rescore --reference-dir ../local-references --output-dir ../ijmlc-rescored
```

The placeholders name user-controlled local files, not bundled data. Preparation preserves original MMQA reference members and M³-VQA alias groups. The rescoring command verifies every supported method/QID score against the released numeric projection; disagreement is an error, not a reason to replace targets.

For the four external configurations, answer strings are not bundled. An optional separately authorized input route is:

```bash
python external_comparisons/replay.py --references ../local-references/locked1341.jsonl --answers ../authorized/selected_answers.jsonl
```

It requires the exact selected-union QIDs and a `methods` dictionary of resolved external answer values. This access arrangement must be established separately. The local candidate validation distinguishes tests using released materials from tests using non-distributed provider references/answer inputs.

## What a passing result means

A passing run verifies frozen records and the named scoring/statistical procedures. It does not verify semantic truth of extracted components, rebuild Expected/Observed states, retrain the selector, or reproduce a commercial backend. Numerical projections and text-based answer rescoring are separate levels of reproduction. M³-VQA uses this study's frozen answer-list implementation, not a claim of official scorer equivalence.
