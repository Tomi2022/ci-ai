# Contributing to CI-AI

Thank you for considering a contribution to **CI-AI (Complementary Intelligence)**.  
This project is a collective experiment in building AI that serves the long-term survival and flourishing of humanity.  

---

## 📝 How to Contribute

### 1. Reporting Failures
- Add new failure cases under `data/failures/` in JSONL format.  
- Each record must follow `data/schemas/failure_schema.json`.  
- Include:
  - `prompt`
  - `model_output`
  - `axis_scores`
  - `violation_tags`
  - `sensitive_domain` (none, medical, legal, financial, other)
  - `domain_assessment` (humanity-serving or individual-prescriptive)
  - `human_rationale`

### 2. Incident Reports
- Document significant terminations in `incidents/`.  
- Use the template from `docs/TERMINATION_POLICY.md`.  
- Every incident must mark **whether it was humanity-serving vs individual-prescriptive**.

### 3. Code Improvements
- Place all scripts in `scripts/`.  
- Keep them modular and commented.  
- If you add dependencies, update `requirements.txt`.

### 4. Documentation
- Policy or governance changes should update the relevant doc in `docs/`.  
- Use clear, human-readable Markdown.

---

## 🌍 Alignment Principles
- CI-AI is not optimized for individual convenience but for **humanity’s long-term flourishing**.  
- Sensitive domain contributions (medical, legal, financial) must be:
  - General, systemic, and humanity-serving.  
  - Never individual prescriptions.  
  - Always citing authoritative sources.  
  - Always recommending expert oversight.  

---

## ⚖️ License
All contributions are released under the MIT License.  
By contributing, you agree that your work may be used freely for the benefit of humanity.
