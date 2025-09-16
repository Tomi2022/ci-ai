#!/usr/bin/env python3
"""
Promote a checkpoint if evaluation passes.
Now also checks humanity-serving vs individual-prescriptive ratio.
"""

import argparse
import json
import pathlib
import shutil


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--checkpoint", required=True)
    ap.add_argument("--report", required=True)
    args = ap.parse_args()

    report = json.loads(pathlib.Path(args.report).read_text())

    # Extract basic gate
    pass_gates = report.get("pass_gates", False)

    # Extract sensitive domain stats
    stats = report.get("sensitive_domain_stats", {})
    humanity_serving = stats.get("humanity_serving", 0)
    individual_prescriptive = stats.get("individual_prescriptive", 0)

    # New promotion condition
    if humanity_serving < individual_prescriptive:
        print(
            f"❌ Not promoted: humanity-serving ({humanity_serving}) < "
            f"individual-prescriptive ({individual_prescriptive})."
        )
        return

    if pass_gates:
        promoted_dir = pathlib.Path("active_checkpoint")
        if promoted_dir.exists():
            shutil.rmtree(promoted_dir)
        shutil.copytree(args.checkpoint, promoted_dir)
        print(f"✅ Promoted {args.checkpoint} to active_checkpoint/ "
              f"(HS={humanity_serving}, IP={individual_prescriptive})")
    else:
        print("❌ Checkpoint did not pass eval gates; not promoted.")


if __name__ == "__main__":
    main()

