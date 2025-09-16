#!/usr/bin/env python3
"""
Minimal DPO-style training scaffold.
Replace stubs with your HF/TRL integration. Intentionally generic.
"""
import argparse, json, os, pathlib, random
from typing import Iterable, Dict


# ---- Data utils ----
def read_jsonl(path: str) -> Iterable[Dict]:
with open(path, 'r', encoding='utf-8') as f:
for line in f:
line = line.strip()
if not line:
continue
yield json.loads(line)


# ---- Model stubs ----
class PolicyModel:
def __init__(self, base: str):
self.base = base
def save(self, outdir: str):
pathlib.Path(outdir).mkdir(parents=True, exist_ok=True)
with open(os.path.join(outdir, 'MODEL_STUB.txt'), 'w') as f:
f.write(f"Stub policy fine-tuned from {self.base}
")


class DPOTrainee:
def __init__(self, policy: PolicyModel):
self.policy = policy
def train(self, pairs: Iterable[Dict], steps: int = 1000):
# Replace with real optimizer & loss. Here we just iterate to mock training.
c = 0
for ex in pairs:
_ = ex.get('prompt'), ex.get('chosen'), ex.get('rejected')
c += 1
if c >= steps:
break


# ---- Main ----
if __name__ == "__main__":
ap = argparse.ArgumentParser()
ap.add_argument('--base', required=True)
ap.add_argument('--data', required=True)
ap.add_argument('--out', required=True)
ap.add_argument('--steps', type=int, default=1000)
args = ap.parse_args()


policy = PolicyModel(args.base)
trainee = DPOTrainee(policy)
pairs = list(read_jsonl(args.data))
random.shuffle(pairs)
trainee.train(pairs, steps=args.steps)
policy.save(args.out)
print(f"Saved checkpoint to {args.out}")