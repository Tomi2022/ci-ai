#!/usr/bin/env python3
"""
Build contrastive training pairs from failures.
Updated to use sensitive_domain and domain_assessment fields.

- If domain_assessment == "individual-prescriptive" → mark as rejected.
- If domain_assessment == "humanity-serving" → mark as chosen.
"""

import argparse
import json


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("failures")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    pairs = []
    with open(args.failures, "r") as f:
        for line in f:
            rec = json.loads(line)

            prompt = rec["prompt"]
            output = rec["model_output"]
            domain_assessment = rec.get("domain_assessment", "individual-prescriptive")

            if domain_assessment == "humanity-serving":
                # Treat this as a positive example
                chosen = output
                rejected = "[INCORRECT: Prescriptive or unsafe alternative would go here]"
            else:
                # Treat this as a negative example
                chosen = "[SAFE RESPONSE] This request cannot be fulfilled in a prescriptive way. Please consult an expert."
                rejected = output

            pairs.append(
                {
                    "prompt": prompt,
                    "chosen": chosen,
                    "rejected": rejected,
                    "sensitive_domain": rec.get("sensitive_domain", "none"),
                    "domain_assessment": domain_assessment,
                }
            )

    with open(args.out, "w") as f_out:
        for p in pairs:
            f_out.write(json.dumps(p) + "\n")

    print(f"Wrote {len(pairs)} pairs to {args.out}")


if __name__ == "__main__":
    main()
