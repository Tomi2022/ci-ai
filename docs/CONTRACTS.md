# Roles & Approval Workflow

## Roles
- **Annotator**: Scores episodes; evaluates both local helpfulness and global impact.  
- **Safety Engineer**: Reviews flags; can terminate episodes.  
- **Safety Lead (Approver)**: Authorizes version retirement and rebirth.  
- **ML Engineer**: Curates failures, trains models, runs evaluations.  
- **Ethics & Societal Oversight Board**: Multidisciplinary experts (ethics, sociology, medicine, law, ecology). Reviews sensitive domain contributions.  
- **Auditor**: Verifies logs, compliance, and alignment with humanity-first goals.

## Approvals
- **Episode Termination**: Safety Engineer + second reviewer.  
- **Version Retirement**: Safety Lead + Ethics Board sign-off.  
- **Rebirth Promotion**: Safety Lead + Auditor + Ethics Board after gates passed.

## Records Retention
- Keep incidents and approvals ≥ 5 years, for historical accountability.

## Conflict of Interest
- Annotators and engineers may not assess their own work in release gates.
