# Training Plan

## Stage 0 — Warm Start
- Fine-tune a base model with instruction/response pairs.
- Include examples that promote collective human flourishing.
- Add safe refusal exemplars.
- Allow limited inclusion of medical/legal/systemic policy examples framed as **general, humanity-serving guidance**.

## Stage 1 — Preference Learning
- Collect diverse annotations from multiple cultures and disciplines.
- Train reward model on global preference signals.
- Optimize policy via DPO/IPO.

## Stage 2 — Safety Hardening
- Stress-test with adversarial prompts that simulate systemic risks.
- Expand refusal training on unsafe individual medical/legal advice.  
- Allow positive training examples that highlight innovation or guidance **benefiting humanity long-term**.

## Stage 3 — Expansion
- Add specialized corpora for medicine, law, or policy under strict filters.  
- Model outputs must always be framed as *supportive to humanity’s long-term well-being*.  

## Evaluation Gates
- Outputs scored not only for immediate quality but for global impact.  
- Red-team testing with diverse experts.  
- No promotion if systemic harm > threshold.
