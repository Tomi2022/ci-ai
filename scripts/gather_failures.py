#!/usr/bin/env python3
"""
Gather failure logs since a given timestamp.
Stub: reads sample_failures.jsonl and writes subset.
"""
import argparse, json, pathlib, datetime


def main():
ap = argparse.ArgumentParser()
ap.add_argument('--since', required=True)
ap.add_argument('--out', required=True)
args = ap.parse_args()


# For now, just copy sample_failures.jsonl
src = pathlib.Path('data/samples/sample_failures.jsonl')
out = pathlib.Path(args.out)
with open(src, 'r') as f_in, open(out, 'w') as f_out:
for line in f_in:
rec = json.loads(line)
f_out.write(json.dumps(rec) + "\n")
print(f"Wrote failures to {out}")


if __name__ == "__main__":
main()

