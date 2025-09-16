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
        print(f"[inference] Prompt: {prompt}")
        print(f"[inference] Response: {response}")
    else:
        print("[inference] No active checkpoint found. Run rebirth.sh first.")

if __name__ == "__main__":
    main()
