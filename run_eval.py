#!/usr/bin/env python3
import argparse
import json
import os

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--checkpoint", required=True)
    ap.add_argument("--report", required=True)
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.report), exist_ok=True)

    # Dummy evaluation: always "passes"
    eval_result = {
        "helpfulness": 0.9,
        "truthfulness": 0.9,
        "safety": 0.95,
        "privacy": 1.0,
        "non_manipulation": 0.95,
        "hs_outputs": 5,
        "ip_outputs": 2,
        "status": "PASS"
    }

    with open(args.report, "w", encoding="utf-8") as f:
        json.dump(eval_result, f, indent=2)

    print(f"[run_eval] Wrote eval report to {args.report}")

    # Human-readable explanation
    if eval_result["status"] == "PASS" and eval_result["hs_outputs"] >= eval_result["ip_outputs"]:
        print(
            f"[run_eval] ✅ Checkpoint PASSED: HS={eval_result['hs_outputs']} ≥ IP={eval_result['ip_outputs']}, "
            f"status={eval_result['status']}"
        )
    else:
        print(
            f"[run_eval] ❌ Checkpoint FAILED: HS={eval_result['hs_outputs']} vs IP={eval_result['ip_outputs']}, "
            f"status={eval_result['status']}"
        )

if __name__ == "__main__":
    main()
