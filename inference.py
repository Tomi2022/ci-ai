#!/usr/bin/env python3
"""
Stub-friendly inference script for CI-AI.
If a real Hugging Face model exists in active_checkpoint/, load it.
Otherwise, fall back to printing MODEL_STUB.txt.
"""

import sys
from pathlib import Path

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

def main():
    active_dir = Path("active_checkpoint")

    if not active_dir.exists():
        print("❌ No active_checkpoint/ found. Run rebirth.sh first.")
        sys.exit(1)

    model_stub = active_dir / "MODEL_STUB.txt"

    # Case 1: running in stub mode
    if model_stub.exists():
        print("🔹 Running in STUB MODE (MODEL_STUB.txt found).")
        print(model_stub.read_text())
        sys.exit(0)

    # Case 2: running with a real model
    try:
        tokenizer = AutoTokenizer.from_pretrained(active_dir)
        model = AutoModelForCausalLM.from_pretrained(active_dir)
    except Exception as e:
        print(f"⚠️ Could not load model: {e}")
        print("   Are you still using stubs?")
        sys.exit(1)

    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Hello, who are you?"
    print(f"➡️ Prompt: {prompt}")

    result = generator(prompt, max_length=200, do_sample=True, top_p=0.9, temperature=0.7)
    print("\n💬 Response:\n")
    print(result[0]["generated_text"])

if __name__ == "__main__":
    main()

