# CI-AI Roadmap

This roadmap outlines the planned milestones for the CI-AI project. 
It is a living document and will evolve as the project grows.

---

## Phase 0 — Foundation (Current)
- [x] Define philosophy and governance docs (Charter, Constitution, Termination Policy, etc.).
- [x] Create repo structure (scripts, data, incidents, docs).
- [x] Add stubs for training pipeline (gather_failures, make_contrastive_pairs, run_eval, promote_checkpoint).
- [x] Set up rebirth cycle script (`rebirth.sh`).
- [x] Add templates for contributions (ISSUE_TEMPLATE, PULL_REQUEST_TEMPLATE, CONTRIBUTING).

**Goal:** Establish an open and transparent framework.

---

##  Phase 1 — Data Growth
- [ ] Expand failure dataset (`data/failures/`).
- [ ] Annotate incidents with humanity-serving vs prescriptive tags.
- [ ] Engage contributors for crowdsourced annotation.
- [ ] Improve contrastive pair generation logic.

**Goal:** Build robust training signals.

---

##  Phase 2 — Training Real Models
- [ ] Replace stubs with Hugging Face fine-tuning code (DPO/IPO).
- [ ] Train first real checkpoints from `sample_failures.jsonl`.
- [ ] Run evaluations and promote models automatically.
- [ ] Deploy inference from `active_checkpoint/`.

**Goal:** Move from simulation → working AI prototypes.

---

##  Phase 3 — Safety Hardening
- [ ] Expand termination criteria for nuanced harms.
- [ ] Adversarial red-teaming (unsafe medical/legal, misinformation, ecological risks).
- [ ] Introduce human-in-the-loop review pipelines.
- [ ] Add dashboards for evaluation metrics.

**Goal:** Ensure robustness and collective safety.

---

##  Phase 4 — Collective Intelligence
- [ ] Open platform for global contributions.
- [ ] Build consensus-based governance for sensitive domain outputs.
- [ ] Explore federation of multiple CI-AI nodes.
- [ ] Release humanity-serving datasets as open commons.

**Goal:** CI-AI as a collective, transparent project serving humanity.

---

##  Phase 5 — Future Directions
- [ ] Integration with external tools (search, simulation) under sandboxed rules.
- [ ] Advanced preference learning from global annotators.
- [ ] Governance models for long-term sustainability (ethics boards, auditors).
- [ ] Potential policy partnerships.

**Goal:** Scale responsibly while remaining open-source and humanity-first.
