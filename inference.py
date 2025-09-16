#!/usr/bin/env python3
import sys
import pathlib

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 inference.py 'your prompt here'")
        return

    prompt = sys.argv[1]
    checkpoint_dir = pathlib.Path("active_checkpoint")
    model_file = checkpoint_dir / "POLICY_STUB.txt"

    if model_file.exists():
        response = model_file.read_text().strip()

        # Detect which run this checkpoint came from
        # (we embed run info inside POLICY_STUB.txt)
        run_info = "unknown run"
        for line in response.splitlines():
            if "data runs/" in line:
                run_info = line.split("data runs/")[1].split("/train_pairs")[0]
                run_info = f"runs/{run_info}"
                break

        print(f"[inference] Active checkpoint: {run_info}")
        print(f"[inference] Prompt: {prompt}")
        print(f"[inference] Response: {response}")
    else:
        print("[inference] No active checkpoint found. Run rebirth.sh first.")

if __name__ == "__main__":
    main()
