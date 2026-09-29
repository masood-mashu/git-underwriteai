"""
dscr_liquidity_calculator.py - Calculates Debt Service Coverage Ratio from Net Operating Income and annual debt service
"""
import sys
import json


def calculate_dscr(financials_json: str):
    import json
    data = json.loads(financials_json) if isinstance(financials_json, str) else financials_json
    noi = data.get("noi_usd", 125000.0)
    service = data.get("annual_debt_service_usd", 100000.0)
    dscr = round(noi / max(service, 1.0), 2)
    is_approved = dscr >= 1.25
    return {"dscr": dscr, "status": "DSCR_APPROVED" if is_approved else "DSCR_DEFICIT"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "dscr-liquidity-calculator"}))
