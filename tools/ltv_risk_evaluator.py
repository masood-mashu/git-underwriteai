"""
ltv_risk_evaluator.py - Calculates Loan-to-Value percentage against certified collateral appraisal
"""
import sys
import json


def evaluate_ltv_risk(collateral_json: str):
    import json
    data = json.loads(collateral_json) if isinstance(collateral_json, str) else collateral_json
    loan = data.get("loan_amount_usd", 700000.0)
    val = data.get("appraised_value_usd", 1000000.0)
    ltv = round((loan / max(val, 1.0)) * 100, 1)
    is_acceptable = ltv <= 75.0
    return {"ltv_pct": ltv, "status": "LTV_ACCEPTABLE" if is_acceptable else "LTV_EXCEEDED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "ltv-risk-evaluator"}))
