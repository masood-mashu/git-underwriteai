# Explainability, Auditability & Decision Logic: GitUnderwriteAI

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitUnderwriteAI**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitUnderwriteAI** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Borrower**: Borrower TTM audited financial statements and rent rolls.
- **Commercial**: Commercial real estate independent MAI appraisal valuations.
- **Federal**: Federal Reserve benchmark SOFR yield curves and bank credit policy manuals.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **calculate_dscr**: Uses `dscr-liquidity-calculator` to calculate calculates debt service coverage ratio from net operating income and annual debt service.
   - **evaluate_ltv_risk**: Uses `ltv-risk-evaluator` to calculate calculates loan-to-value percentage against certified collateral appraisal.
   - **benchmark_credit_spread**: Uses `credit-spread-benchmarker` to calculate spreads interest margin against sofr baseline according to borrower risk tier.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When a loan package is submitted, the agent runs dscr_liquidity_calculator, ltv_risk_evaluator, and credit_spread_benchmarker. If DSCR >= 1.25, LTV <= 75%, and borrower covenants hold, it issues APPROVED. If DSCR is between 1.15 and 1.24, it issues NEEDS_REVIEW. If DSCR < 1.15 or LTV > 80%, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on standard banking formulas.
- **Does**: Does not replace human appraisal verification of physical collateral condition.
- **Assumes**: Assumes provided financial statements are verified by licensed CPA auditors.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
