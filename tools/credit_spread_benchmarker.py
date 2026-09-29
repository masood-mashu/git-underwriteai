"""
credit_spread_benchmarker.py - Spreads interest margin against SOFR baseline according to borrower risk tier
"""
import sys
import json


def benchmark_credit_spread(risk_tier_json: str):
    import json
    data = json.loads(risk_tier_json) if isinstance(risk_tier_json, str) else risk_tier_json
    tier = data.get("risk_tier", "A").upper()
    sofr = data.get("sofr_rate", 5.25)
    spread = 2.0 if tier == "A" else (2.75 if tier == "B" else 4.0)
    final_rate = round(sofr + spread, 2)
    return {"spread_bps": int(spread * 100), "all_in_rate": final_rate, "status": "SPREAD_CALIBRATED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "credit-spread-benchmarker"}))
