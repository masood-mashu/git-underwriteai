"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitUnderwriteAI.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.dscr_liquidity_calculator import *
from tools.ltv_risk_evaluator import *
from tools.credit_spread_benchmarker import *

class TestGitUnderwriteAIPredictability(unittest.TestCase):
    def test_dscr_liquidity_calculator(self):
        res = calculate_dscr('{"noi_usd": 150000.0, "annual_debt_service_usd": 100000.0}')
        self.assertEqual(res["dscr"], 1.5)
        self.assertEqual(res["status"], "DSCR_APPROVED")

    def test_ltv_risk_evaluator(self):
        res = evaluate_ltv_risk('{"loan_amount_usd": 650000.0, "appraised_value_usd": 1000000.0}')
        self.assertEqual(res["ltv_pct"], 65.0)
        self.assertEqual(res["status"], "LTV_ACCEPTABLE")

    def test_credit_spread_benchmarker(self):
        res = benchmark_credit_spread('{"risk_tier": "A", "sofr_rate": 5.0}')
        self.assertEqual(res["spread_bps"], 200)
        self.assertEqual(res["status"], "SPREAD_CALIBRATED")


if __name__ == "__main__":
    unittest.main()
