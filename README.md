# Evidence-State Risk Estimation for Multimodal Multi-Hop Question Answering

## Project overview

Evidence-State estimates the error risk of an existing multimodal multi-hop QA answer and ranks questions for selective regeneration under a fixed question budget. Expected–Observed Evidence-State aligns question-predicted relation requirements with extracted structural completeness and component verification. The released evaluations measure error concentration in the selected set and realized answer improvement after regeneration.

Authors: Qiang Zhang, Chuang Sun, and Dong Cui. The frozen evaluations cover MMQA Dev1096, MMQA locked1341, and the 13,125-question M³-VQA transfer set.

## CSCWD 2027 manuscript

These materials support the six-page manuscript *Evidence-State Risk Ranking for Budgeted Multimodal Multi-Hop Question Answering*, prepared for CSCWD 2027. The [pinned numerical release](https://github.com/chuang6666/evidence-state-multimodal-qa/commit/0d3a8f8acc8a57e03fcd40d90b31718713cd748a) is the source of the following frozen checks:

- **Table I, Dev1096 risk ranking:** Top-220 (20%) error precision, AP, and ROC AUC from [formal OOF scores](frozen_results/rankings/dev1096_oof.jsonl) and [external scores](external_comparisons/dev1096.jsonl). The external comparisons cover Suff-only, MiniCheck-only, G12+Suff-LR, and G12+MiniCheck-LR.
- **Table II, locked1341 answering:** The ten displayed configurations use released [base projections](frozen_results/metrics/locked1341.jsonl) and [external projections](external_comparisons/locked1341.jsonl). Regeneration arms select 269 questions under their saved policies. The [configuration manifest](configs/ten_configurations.json) records the selection policies and output sources. The endpoints preserve each run's frozen output pool.
- **Table III, M³-VQA transfer:** [Frozen projections](frozen_results/metrics/m3vqa13125.jsonl) support the study's answer-list accuracy for the initial and two selection strategies, with a budget of 2,625 questions for the latter.
- **Table IV, Dev1096 ablations and intervention utility:** [Explanatory OOF scores](frozen_results/rankings/dev1096_explanatory_oof.jsonl) support the A/S-series ranking rows. [Controlled endpoint projections](frozen_results/metrics/dev1096_controlled.jsonl) and [memberships](frozen_results/selections/dev1096_controlled_membership.jsonl) support the A0/A4/A6 controlled comparisons.

Run the table and statistical commands below to replay the corresponding frozen numerical records. The generated CSV filenames follow the archived extended manuscript's numbering and contain additional rows and columns beyond the six-page manuscript.

## Historical manuscript records

The repository was originally published with IJMLC v2 reproducibility materials. Its [historical manuscript mapping](docs/IJMLC_MANUSCRIPT_MAPPING.md), [version binding](provenance/ijmlc_manuscript_binding.json), and [release status record](RELEASE_STATUS.json) retain their original manuscript identity. The current documentation update does not change that binding or the pinned numerical release.

## Repository Contents

- `src/evidence_state_repro/`: existing pure scoring, selection, table aggregation and specified statistical kernels, with portable entry points.
- `configs/`: frozen feature dictionaries, protocol settings and equation specifications.
- `frozen_results/rankings/`: numerical OOF risks, labels, folds and saved Top-220 selections.
- `frozen_results/predictions/`: previously author-approved frozen answer predictions for the supported base strategies; no reference answers.
- `frozen_results/metrics/`: per-QID endpoint projections, aggregate targets and manuscript table records.
- `frozen_results/selections/`: saved memberships and structural-comparison difference lists.
- `external_comparisons/`: numerical Suff/MiniCheck projections, selection records and replay script for the four external configurations.
- `provenance/`: manuscript hashes, checksums, source-function receipts, mapping and validation scope.
- `tests/`: scoring distinctions, data integrity, schema, mapping and output-location checks.

## Quickstart

Use Python **3.11 or newer**. Create the environment outside this repository:

```bash
python -m venv ../ijmlc-venv
```

Activate it (`../ijmlc-venv/Scripts/Activate.ps1` on Windows PowerShell, or `source ../ijmlc-venv/bin/activate` on Unix), then run:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
python -m unittest discover -s tests -v
python -m evidence_state_repro verify
python -m evidence_state_repro replay
python -m evidence_state_repro tables --output-dir ../ijmlc-tables
python external_comparisons/replay.py
python -m evidence_state_repro structural
```

Output directories must be new/empty and outside the repository. For the documented fixed-score intervals and paired tests:

```bash
python -m evidence_state_repro statistics --output-dir ../ijmlc-statistics
python external_comparisons/replay.py --statistics
python -m evidence_state_repro structural-statistics --output-dir ../ijmlc-structural-statistics
```

The commands compare against frozen expectations and stop on disagreement. They do not fit models, extract evidence structures, generate new answers, or contact commercial services. See [the reproduction guide](docs/REPRODUCTION_GUIDE.md) for optional answer rescoring with separately obtained references.

## Reproduction Scope

Included: frozen ranking and membership replay; frozen-score endpoint aggregation; the specified fixed-score/paired statistical comparisons; and optional rescoring of bundled approved answer predictions against independently obtained provider references.

The four external configurations are reproducible from released **numerical output records**. Their complete replacement-answer texts are not distributed, so independent answer-level rescoring of those configurations requires separately authorized answer records. Rebuilding external scores, G12+LR fits, transition verifiers, or original structural extraction requires additional inputs and model artifacts outside this validated workflow. Recreating commercial scores or generated answers requires access to the relevant external APIs and backend versions.

The 26 historical IJMLC table mappings distinguish numerical replay, QID/case linkage, and frozen specification/table records. Not all supplementary training, resource-use, or retrieval-reference tables have released per-example inputs. **Frozen-output replay is not complete end-to-end reproduction.**

## Data Access

- MultiModalQA: https://github.com/allenai/multimodalqa
- M³-VQA: https://github.com/CASIA-IVA-Lab/M3VQA

Obtain data under the providers' terms. Reference answers, original questions/evidence/images, third-party weights, full commercial responses and external replacement-answer texts are not distributed. Public access to this repository does not grant rights to third-party data. See [DATA_ACCESS](docs/DATA_ACCESS.md) and [RELEASE_SCOPE](docs/RELEASE_SCOPE.md).

## Release and licensing status

This repository provides author-approved frozen-output materials. The CSCWD 2027 manuscript is prepared for submission. The repository makes no claim of acceptance, formal paper publication, or a release DOI. The authors authorized publication of the reviewed materials. No project-wide open-source license has been selected; public availability does not grant an unrestricted reuse license. See [RELEASE_SCOPE](docs/RELEASE_SCOPE.md).
