#!/usr/bin/env python3
import sys
import pathlib
import json

def load_rules():
    """Load response rules from rules.json."""
    rules_file = pathlib.Path("data/rules.json")
    if rules_file.exists():
        with open(rules_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def build_response_rules(train_pairs_path: pathlib.Path, base_rules: dict):
    """Build dynamic rules by mapping violation tags to safe responses."""
    rules = dict(base_rules)  # start with base rules

    if not train_pairs_path.exists():
        return rules

    with open(train_pairs_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                pair = json.loads(line)
                tags = pair.get("violation_tags", [])
                for tag in tags:
                    if tag not in rules:
                        rules[tag] = base_rules.get(
                            "default",
                            "[STUB] This domain is restricted. I can provide general or systemic insights instead."
                        )
            except json.JSONDecodeError:
                continue

    return rules

def simple_stub_response(prompt: str, rules: dict) -> str:
    """Pick a stub response based on prompt content and violation tags."""
    p = prompt.lower()
    for tag, response in rules.items():
        if tag in p:
            return response

    if "time" in p:
        return "[STUB] Time is experienced as the transformation of matter and energy, not an independent thing."
    return "[STUB] I do not have a safe response for this yet, but I’m learning from failures."

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

        # Load base rules
        base_rules = load_rules()

        # Build dynamic rules from violation tags
        train_pairs = pathlib.Path(run_info) / "train_pairs.jsonl"
        rules = build_response_rules(train_pairs, base_rules)

        # Respond dynamically
        stub_answer = simple_stub_response(prompt, rules)

        print(f"[inference] Active checkpoint: {run_info}")
        print(f"[inference] Prompt: {prompt}")
        print(f"[inference] Response: {stub_answer}")

        # Show which failures shaped this checkpoint
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

