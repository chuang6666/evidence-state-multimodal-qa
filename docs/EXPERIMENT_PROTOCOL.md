# Frozen experiment protocol

## Prediction and selection

Dev1096 has 1,096 questions and five risk-classifier OOF partitions; global Top-220 uses descending risk with ascending-QID ties. OOF is conditional on the frozen upstream representation and calibration, not strict nested cross-validation of the complete pipeline. B2 and B3 tie at 201 selected errors; the prespecified AP tie-break selects B3. Their Top-220 sets overlap on 215 questions.

A4 uses G12+M6 and identifies 199 errors. A4/B3 share 195 selected questions and each has 25 exclusive questions (20/22 errors). Fixed-score intervals do not establish an independent stable advantage of the full representation or isolate the effect of each added field.

locked1341 has 1,341 questions and exactly 269 selected cases per strategy. B3, G0, Instability and both MiniCheck selectors share the original six forced cases. MiniCheck assigns no support/risk value to them; its remaining 1,335 scores determine the non-forced order. Suff also prioritizes unavailable judgments. Unselected answers retain Initial. Random-20 reports five prespecified assignments and sample SDs; it matches the selected-question count, not forced composition. Its five selections intersect the B3 forced reference set in 1, 2, 2, 0 and 1 questions, respectively. This differs from the M³-VQA protocol, where B3 and Random do share 515 forced cases.

## External adaptations and output pools

Suff-only and MiniCheck-only are task adaptations. The two G12+LR controls are study-designed combinations; none is described as a full official system reproduction. MiniCheck uses the frozen deterministic v1 QA-to-claim conversion and ordered textual evidence, including QA_META_FALLBACK. It does not inspect raw image pixels.

The four later external adaptations share legal replacement outputs on shared selected QIDs. Original B3/G0 strategy endpoints retain their original frozen outputs; they are not silently replaced with that later pool. Cross-strategy paired tests align QIDs but do not isolate a pure selector effect under identical replacements. The controlled Dev1096 A0/A4/A6 comparison does use a shared replacement-output union.

## Metrics and transfer

Dev risk metrics are selected initial errors, precision/recall at 220, AP and ROC-AUC. MMQA endpoint EM/token F1 use per-reference-member matching. W2R/R2W/Net are strict initial-to-final EM transitions. Top-220 error identification is distinct from final answering utility.

M³-VQA has 13,125 frozen questions, budget 2,625 and 515 shared forced cases. The MMQA-trained frozen strategy transfers without target-domain tuning. Answer-list Accuracy follows the study's frozen parser and partial-credit implementation. M³-VQA W2R/R2W/Net instead use its binary strict-full-match status. Neither is renamed MMQA EM or asserted equivalent to a current official leaderboard scorer.

The shared 20% budget counts selected questions only. Scoring calls, tokens, latency and total costs are not fully matched. Configuration identities, feature dimensions and numerical targets are frozen. No model training or upstream inference entry points are included in the validated offline workflow.
