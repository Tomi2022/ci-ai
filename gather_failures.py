#!/usr/bin/env python3
import argparse
import json
import os
import glob

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", required=True, help="Date cutoff for failures (YYYY-MM-DD)")
    ap.add_argument("--out", required=True, help="Output JSONL file")
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    # Collect failures from both samples and user-contributed failures
    sources = glob.glob("data/samples/*.jsonl") + glob.glob("data/failures/*.jsonl")

    count = 0
    with open(args.out, "w", encoding="utf-8") as dst:
        for src_file in sources:
            with open(src_file, "r", encoding="utf-8", errors="ignore") as src:
                for line in src:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        failure = json.loads(line)
                        # (Optional) filter by date if failures include a date field
                        dst.write(json.dumps(failure) + "\n")
                        count += 1
                    except json.JSONDecodeError:
                        print(f"[gather_failures] Skipped invalid line in {src_file}: {line[:50]}...")

    print(f"[gather_failures] Wrote {count} failures to {args.out}")

if __name__ == "__main__":
    main()
