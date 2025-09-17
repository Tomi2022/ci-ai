#!/usr/bin/env python3
import argparse
import os
import json

class DummyTrainer:
    def __init__(self, base, data, out):
        self.base = base
        self.data = data
        self.out = out

    def train(self):
        os.makedirs(self.out, exist_ok=True)

        # Count training pairs
        num_pairs = 0
        try:
            with open(self.data, "r", encoding="utf-8") as f:
                for _ in f:
                    num_pairs += 1
        except FileNotFoundError:
            print(f"[train_dpo] WARNING: data file {self.data} not found, using 0 pairs")

        checkpoint_file = os.path.join(self.out, "POLICY_STUB.txt")
        with open(checkpoint_file, "w", encoding="utf-8") as f:
            f.write(
                f"Stub policy fine-tuned from {self.base} using data {self.data} "
                f"with {num_pairs} training pairs.\n"
            )

        print(f"[train_dpo] Wrote stub checkpoint to {checkpoint_file}")
        print(f"[train_dpo] Used {num_pairs} training pairs")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    trainer = DummyTrainer(args.base, args.data, args.out)
    trainer.train()

if __name__ == "__main__":
    main()
