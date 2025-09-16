#!/usr/bin/env python3
import sys
import pathlib
import json

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 inference.py 'your prompt here'")
        return

    prompt = sys.argv[1]
    checkpoint_dir = pathlib.Path("active_checkpoint")
    model_file = checkpoint_dir / "POLICY_STUB.txt"

    if model_file.exists():
        response = model_file.read_text().strip()

        # Extract run info
        run_info = "unknown run"
        for line in response.splitlines():
            if "data runs/" in line:
                run_info = line.split("data runs/")[1].split("/train_pairs")[0]
                run_info = f"runs/{run_info}"
                break

        print(f"[inference] Active checkpoint: {run_info}")
        print(f"[inference] Prompt: {prompt}")
        print(f"[inference] Response: {response}")

        # Try to show which failures shaped it
        train_pairs = pathlib.Path(run_info) / "train_pairs.jsonl"
        if train_pairs.exists():
            ids = []
            with open(train_pairs, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        pair = json.loads(line)
                        if "id" in pair:
                            ids.append(pair["id"])
                    except json.JSONDecodeError:
                        continue
            if ids:
                print(f"[inference] Shaped by failure IDs: {', '.join(ids)}")
            else:
                print("[inference] No failure IDs found in train_pairs.jsonl")
        else:
            print("[inference] Could not locate train_pairs.jsonl for this checkpoint")

    else:
        print("[inference] No active checkpoint found. Run rebirth.sh first.")

if __name__ == "__main__":
    main()
