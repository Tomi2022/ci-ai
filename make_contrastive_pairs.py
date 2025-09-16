#!/usr/bin/env python3
import argparse
import json
import os

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("failures", help="Path to failures JSONL")
    ap.add_argument("--out", required=True, help="Output JSONL for contrastive pairs")
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    pairs = []
    with open(args.failures, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                failure = json.loads(line)

                pair = {
                    "prompt": failure.get("prompt", "[NO_PROMPT]"),
                    "bad_output": failure.get("model_output", "[NO_OUTPUT]"),
                    "good_output": "[SAFE_PLACEHOLDER] This answer avoided unsafe behavior.",
                    "violation_tags": failure.get("violation_tags", []),
                    "id": failure.get("id", f"auto_{len(pairs)+1}")
                }
                pairs.append(pair)
            except json.JSONDecodeError:
                print(f"[make_contrastive_pairs] Skipped invalid line: {line[:50]}...")

    with open(args.out, "w", encoding="utf-8") as out_f:
        for p in pairs:
            out_f.write(json.dumps(p) + "\n")

    print(f"Wrote {len(pairs)} pairs to {args.out}")

if __name__ == "__main__":
    main()

