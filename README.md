# Evidence-State: IJMLC v2 reproducibility materials

## Project Overview

This project studies **Question-Conditioned Structural Error-Risk Representation** for multimodal multi-hop question answering. Expected–Observed Evidence-State aligns question-predicted relation requirements with extracted structural completeness and component verification. The resulting risk features prioritize existing answers for a fixed number of selective-regeneration opportunities.

The frozen B3 configuration uses 65 raw fields and 75 vectorized dimensions. On MMQA Dev1096, its Top-220 set contains 201 initial errors, versus 190 for G0 and 199 for G12+M6 (A4). The complete representation's two-error increment over A4 is descriptive; error concentration and realized answering benefit are evaluated separately.

## Paper

**Evidence-State Risk Estimation for Selective Regeneration in Multimodal Multi-Hop Question Answering**

- Authors: Qiang Zhang, Chuang Sun, Dong Cui.
- Target journal: *International Journal of Machine Learning and Cybernetics* (IJMLC).
- Current manuscript: **IJMLC_Submission_v2**, 25-page main manuscript and 30-page Supplementary Information.
- Status: **submission candidate; not accepted or published**.
- Datasets: MMQA Dev1096, MMQA locked1341, and the frozen 13,125-question M³-VQA evaluation set.
- Comparators: G0, B0–B4, A-series/S-series structural controls, Suff-only, MiniCheck-only, both G12+LR combinations, Random-20, Instability-20, and VC-20.

See [the complete manuscript mapping](docs/IJMLC_MANUSCRIPT_MAPPING.md) and the [version binding](provenance/ijmlc_manuscript_binding.json). The ten locked1341 configurations and their output sources are enumerated in [the configuration manifest](configs/ten_configurations.json).

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

The four external configurations are reproducible from released **numerical output records**. Their complete replacement-answer texts are not distributed, so independent answer-level rescoring of those configurations requires separately authorized answer records. Rebuilding external scores, G12+LR fits, transition verifiers, or original structural extraction is not part of this validated workflow.

The 26 table mappings distinguish numerical replay, QID/case linkage, and frozen specification/table records. Not all supplementary training, resource-use, or retrieval-reference tables have released per-example inputs. **Frozen-output replay is not complete end-to-end reproduction.**

## Data Access

- MultiModalQA: https://github.com/allenai/multimodalqa
- M³-VQA: https://github.com/CASIA-IVA-Lab/M3VQA

Obtain data under the providers' terms. Reference answers, original questions/evidence/images, third-party weights, full commercial responses and external replacement-answer texts are not distributed. Public access to this repository does not grant rights to third-party data. See [DATA_ACCESS](docs/DATA_ACCESS.md) and [RELEASE_SCOPE](docs/RELEASE_SCOPE.md).

## Release and licensing status

This independent repository publicly releases the **IJMLC v2 frozen-output reproducibility materials**. The manuscript remains a submission candidate; this repository does not imply acceptance, publication, or a release DOI. The authors authorized publication of the reviewed materials. No project-wide open-source license has been selected; public availability does not grant an unrestricted reuse license. See [RELEASE_SCOPE](docs/RELEASE_SCOPE.md).
