# IJMLC v2 manuscript-to-material mapping

Bound version: 25-page main manuscript, 30-page SI; 34 scientific references; 9 main + 17 SI tables; 13 equation environments. Artifact hashes are in `provenance/ijmlc_manuscript_binding.json`.

## Scope labels

`NUMERICAL_REPLAY` means a frozen numeric aggregator is available. `FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY` means a checked specification/saved table is supplied, not a claim of upstream reproduction. `QID_TRANSITION_MAPPING_ONLY` links cases without distributing their evidence. All paths below are real files in this candidate. Validation outcomes are recorded in `provenance/validation.json`.

## All manuscript tables

| Table | Material paths | Scope |
|---|---|---|
| 1 | `frozen_results/metrics/manuscript_tables.json`<br>`configs/equation_contracts.json`<br>`configs/clean_risk_feature_contract.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| 2 | `frozen_results/metrics/manuscript_tables.json`<br>`frozen_results/rankings/dev1096_oof.jsonl`<br>`src/evidence_state_repro/offline.py` | NUMERICAL_REPLAY |
| 3 | `frozen_results/metrics/manuscript_tables.json`<br>`external_comparisons/dev1096.jsonl`<br>`external_comparisons/replay.py`<br>`src/evidence_state_repro/ijmlc_tables.py` | NUMERICAL_REPLAY |
| 4 | `frozen_results/metrics/manuscript_tables.json`<br>`frozen_results/metrics/locked1341.jsonl`<br>`external_comparisons/locked1341.jsonl`<br>`src/evidence_state_repro/ijmlc_tables.py` | NUMERICAL_REPLAY |
| 5 | `frozen_results/metrics/manuscript_tables.json`<br>`frozen_results/selections/locked1341_all_selector_membership.jsonl`<br>`external_comparisons/locked1341.jsonl`<br>`src/evidence_state_repro/ijmlc_tables.py` | NUMERICAL_REPLAY |
| 6 | `frozen_results/metrics/manuscript_tables.json`<br>`frozen_results/metrics/m3vqa13125.jsonl`<br>`src/evidence_state_repro/m3_frozen.py`<br>`src/evidence_state_repro/offline.py` | NUMERICAL_REPLAY |
| 7 | `frozen_results/metrics/manuscript_tables.json`<br>`frozen_results/rankings/dev1096_explanatory_oof.jsonl`<br>`configs/exact_variant_key_sets.json`<br>`src/evidence_state_repro/offline.py` | NUMERICAL_REPLAY |
| 8 | `frozen_results/metrics/manuscript_tables.json`<br>`frozen_results/metrics/dev1096_controlled.jsonl`<br>`frozen_results/selections/dev1096_controlled_membership.jsonl`<br>`src/evidence_state_repro/offline.py` | NUMERICAL_REPLAY |
| 9 | `frozen_results/metrics/manuscript_tables.json`<br>`frozen_results/metrics/qualitative_case_qid_map.json` | QID_TRANSITION_MAPPING_ONLY |
| S1 | `frozen_results/metrics/manuscript_tables.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S2 | `frozen_results/metrics/manuscript_tables.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S3 | `frozen_results/metrics/manuscript_tables.json`<br>`frozen_results/metrics/m3vqa13125.jsonl` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S4 | `frozen_results/metrics/manuscript_tables.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S5 | `frozen_results/metrics/manuscript_tables.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S6 | `frozen_results/metrics/manuscript_tables.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S7 | `frozen_results/metrics/manuscript_tables.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S8 | `frozen_results/metrics/manuscript_tables.json`<br>`configs/exact_variant_key_sets.json`<br>`configs/clean_risk_feature_contract.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S9 | `frozen_results/metrics/manuscript_tables.json`<br>`configs/exact_variant_key_sets.json`<br>`configs/clean_risk_feature_contract.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S10 | `frozen_results/metrics/manuscript_tables.json`<br>`configs/exact_variant_key_sets.json`<br>`configs/clean_risk_feature_contract.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S11 | `frozen_results/metrics/manuscript_tables.json`<br>`configs/exact_variant_key_sets.json`<br>`configs/clean_risk_feature_contract.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S12 | `frozen_results/metrics/manuscript_tables.json`<br>`configs/exact_variant_key_sets.json`<br>`configs/clean_risk_feature_contract.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S13 | `frozen_results/metrics/manuscript_tables.json`<br>`configs/exact_variant_key_sets.json`<br>`configs/clean_risk_feature_contract.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S14 | `frozen_results/metrics/manuscript_tables.json`<br>`configs/exact_variant_key_sets.json`<br>`configs/clean_risk_feature_contract.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S15 | `frozen_results/metrics/manuscript_tables.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S16 | `frozen_results/metrics/manuscript_tables.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |
| S17 | `frozen_results/metrics/manuscript_tables.json` | FROZEN_CONTRACT_OR_TABLE_RECORD_ONLY |

## Configurations and populations

- **B3/G0/B2**: `frozen_results/rankings/dev1096_oof.jsonl`; `src/evidence_state_repro/offline.py`.
- **A4/B3**: `frozen_results/rankings/dev1096_explanatory_oof.jsonl`, `frozen_results/rankings/a4_b3_per_qid_ranks.csv`, `frozen_results/metrics/structural_increment_expected.json`, `src/evidence_state_repro/structural_replay.py`.
- **B2/B3**: formal OOF file plus the same structural replay; overlap 215, each has five exclusive QIDs; AP tie-break retained.
- **Suff-only, MiniCheck-only, G12+Suff-LR, G12+MiniCheck-LR**: `external_comparisons/dev1096.jsonl`, `locked1341.jsonl`, `expected.json`, `replay.py`.
- **Naming**: the requested shorthands “Suff-LR” and “MiniCheck-LR” are not additional frozen experiments. The actual direct adaptations are Suff-only/MiniCheck-only; LR belongs to the explicitly named G12 combinations. Main endpoint display names Suff-20/MiniCheck-20 refer to those direct adaptations.
- **Dev1096**: `frozen_results/rankings/`; controlled answers/endpoints in `frozen_results/predictions/dev1096_controlled.jsonl` and `frozen_results/metrics/dev1096_controlled.jsonl`.
- **locked1341**: base and external metric files in Table 4 mapping; all ten display-to-record names and output sources in `configs/ten_configurations.json`.
- **M³-VQA**: `frozen_results/metrics/m3vqa13125.jsonl`, `frozen_results/selections/m3vqa13125_selection.jsonl`, `src/evidence_state_repro/m3_frozen.py`.

## Figures and equations

- **Figure 1**: method specification in `configs/clean_risk_feature_contract.json`, `exact_variant_key_sets.json`, `equation_contracts.json`; no claim that upstream extraction can be rerun from this release.
- **Figure 2**: missing-first and verification-state rules in `configs/equation_contracts.json` and `docs/EXPERIMENT_PROTOCOL.md`; illustrative mechanisms, not new evaluation cases.
- **Figure 3**: data from numerical Tables 2, 4 and 6 reproduced by `src/evidence_state_repro/ijmlc_tables.py`. Its main-paper comparator subset is preserved; the complete external comparison remains Tables 3–5.
- **Equations 1–12 and SI equation 1**: exact frozen mathematical specifications in `configs/equation_contracts.json`. Selection, risk metric, strict transitions and answer-list scoring have executable frozen kernels. Expected/Observed extraction and LR refitting do not have a validated upstream execution route here.

## Statistical analyses

`src/evidence_state_repro/statistics_run.py` covers the 24 named baseline/component checks. `external_comparisons/replay.py --statistics` covers the specified four external paired comparisons. `src/evidence_state_repro/structural_replay.py` covers SI S6.3 fixed-score structural comparisons. Resource/training/retrieval-reference SI records are not mislabeled as rerun experiments.

## Output provenance

The four later adaptations share legal replacements on overlapping selections. Original B3/G0 endpoints retain their frozen outputs. QID pairing across those strategies is not identical-output-pool pairing. The controlled A0/A4/A6 experiment has its separately documented shared output pool. See `configs/ten_configurations.json` and `docs/EXPERIMENT_PROTOCOL.md`.

## Additional frozen random memberships

`frozen_results/selections/locked1341_random_five_assignments.jsonl` preserves actual five-seed memberships and original selection positions from the frozen plan: 269 per seed. MMQA Random matches the question count, not forced composition; its intersections with the B3 forced reference set are 1, 2, 2, 0 and 1. The `b3_forced_reference` field is not a Random inclusion rule. `frozen_results/selections/m3vqa_random20_selection.jsonl` preserves the actual 2,625-case random selection and 515 forced cases. Neither is inferred from changed answers or generated by a new random draw.
