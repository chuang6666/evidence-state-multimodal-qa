# Data access and restrictions

Official provider repositories, checked for this candidate:

- **MultiModalQA**: https://github.com/allenai/multimodalqa
- **M³-VQA**: https://github.com/CASIA-IVA-Lab/M3VQA

Follow each provider's current download instructions, attribution requirements and data/asset terms. No new permission or dataset license is granted here. Image and source-document rights may differ from the code repository's terms.

The released data contain opaque benchmark QIDs, frozen numeric risks/labels/scores, selection membership and previously author-approved prediction values. They contain no benchmark reference-answer fields, original questions/evidence, raw images or third-party weights. The numeric initial-error labels and score derivatives are study outputs; they are not a distribution of reference-answer strings.

## Reference inputs for optional rescoring

MMQA input is JSONL (plain or gzip) with unique `qid` or `question_id` and original `answers`. M³-VQA input is the provider `quesions.jsonl` (provider spelling), with `data_id` and original `answer_evals` alias groups. Frozen M³-VQA QIDs map to `data_id`.

The preparation command makes local-only `locked1341.jsonl` (1,341), `dev1096_controlled.jsonl` (1,096) and `m3vqa13125.jsonl` (13,125). These canonical reference files must remain outside this repository. Missing QIDs, malformed reference groups and score disagreement stop the workflow.

External Suff/MiniCheck replacement-answer texts are not included; numerical replay requires no such text. Independent rescoring of those methods requires separately authorized resolved answers. Do not infer that permission or an access-on-request service exists merely because evaluation code is public.

Do not upload local provider downloads, Gold, source evidence, images, full API responses, model weights, credentials, or unpublished semantic-audit materials with this repository.
