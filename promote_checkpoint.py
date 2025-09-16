#!/usr/bin/env python3
import argparse
import json
import os
import pathlib
import shutil

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--checkpoint", required=True)
    ap.add_argument("--report", required=True)
    args = ap.parse_args()

    report_path = pathlib.Path(args.report)
    if not report_path.exists():
        print(f"[promote_checkpoint] ERROR: report file {args.report} not found")
        return

    report = json.loads(report_path.read_text())

    # Check HS ≥ IP and status PASS
    if report.get("status") == "PASS" and report.get("hs_outputs", 0) >= report.get("ip_outputs", 0):
        target_dir = pathlib.Path("active_checkpoint")
        os.makedirs(target_dir, exist_ok=True)
        for item in pathlib.Path(args.checkpoint).iterdir():
            if item.is_file():
                shutil.copy(item, target_dir / item.name)
        print(f"[promote_checkpoint] Promoted checkpoint {args.checkpoint} → {target_dir}")
    else:
        print("[promote_checkpoint] Checkpoint not promoted (failed evaluation).")

if __name__ == "__main__":
    main()


