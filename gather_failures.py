#!/usr/bin/env python3
import argparse
import json
import os

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", required=True, help="Date cutoff for failures (YYYY-MM-DD)")
    ap.add_argument("--out", required=True, help="Output JSONL file")
    args = ap.parse_args()

    # For now, just copy sample failures into output
    sample_file = "data/samples/sample_failures.jsonl"
    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    # Open with safe decoding to handle any stray characters
    with open(sample_file, "r", encoding="utf-8", errors="ignore") as src, \
         open(args.out, "w", encoding="utf-8") as dst:
        count = 0
        for line in src:
            line = line.strip()
            if not line:
                continue
            try:
                json.loads(line)  # validate JSON
                dst.write(line + "\n")
                count += 1
            except json.JSONDecodeError:
                print(f"[gather_failures] Skipped invalid JSON line: {line[:50]}...")

    print(f"[gather_failures] Wrote {count} failures to {args.out}")

if __name__ == "__main__":
    main()
