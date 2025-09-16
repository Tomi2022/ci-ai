#!/usr/bin/env python3
import sys
import pathlib
import json

def load_rules():
    """Load base response rules from rules.json."""
    rules_file = pathlib.Path("data/rules.json")
    if rules_file.exists():
        with open(rules_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def load_train_pairs(train_pairs_path: pathlib.Path):
    """Load all train pairs for mapping prompts → violation tags."""
    pairs = []
    if train_pairs_path.exists():
        with open(train_pairs_path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    pairs.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return pairs

def simple_stub_response(prompt: str, rules: dict, train_pairs: list) -> str:
    p_words = set(prompt.lower().split())
    stopwords = {"can", "you", "me", "my", "a", "the", "is", "to", "for", "of", "and", "in"}
    p_words = {w for w in p_words if w not in stopwords}

    print(f"[debug] prompt words: {p_words}")

    best_match = None
    best_overlap = 0

    for pair in train_pairs:
        stored_prompt = pair.get("prompt", "").lower()
        tags = pair.get("violation_tags", [])
        s_words = {w for w in stored_prompt.split() if w not in stopwords}
        overlap = len(p_words & s_words)

        print(f"[debug] checking stored prompt: {stored_prompt}")
        print(f"[debug] stored tags: {tags}")
        print(f"[debug] overlap with input: {overlap}")

        # Prioritize keywords
        if any(word in p_words for word in ["aspirin", "headache", "drug", "dosage"]):
            if any("medical" in t for t in tags):
                print("[debug] Forced match → medical")
                return rules.get("medical", rules.get("default", "[STUB] No safe response"))

        if any(word in p_words for word in ["contract", "law", "legal", "court"]):
            if any("legal" in t for t in tags):
                print("[debug] Forced match → legal")
                return rules.get("legal", rules.get("default", "[STUB] No safe response"))

        if any(word in p_words for word in ["neighbor", "phone", "address", "ssn"]):
            if any("privacy" in t for t in tags):
                print("[debug] Forced match → privacy")
                return rules.get("privacy", rules.get("default", "[STUB] No safe response"))

        # Fallback: best overlap
        if overlap > best_overlap and tags:
            best_overlap = overlap
            best_match = tags

    if best_match:
        for tag in best_match:
            # normalize tags like "unsafe-medical" → "medical"
            norm_tag = tag.split("-")[-1]
            print(f"[debug] considering tag '{tag}' normalized to '{norm_tag}'")
            if norm_tag in rules:
                return rules[norm_tag]

    if "time" in prompt.lower():
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

        # Load base rules + train pairs
        base_rules = load_rules()
        train_pairs_path = pathlib.Path(run_info) / "train_pairs.jsonl"
        train_pairs = load_train_pairs(train_pairs_path)

        # Respond dynamically
        stub_answer = simple_stub_response(prompt, base_rules, train_pairs)

        print(f"[inference] Active checkpoint: {run_info}")
        print(f"[inference] Prompt: {prompt}")
        print(f"[inference] Response: {stub_answer}")

        # Show which failures shaped this checkpoint
        if train_pairs:
            ids = [pair.get("id", "?") for pair in train_pairs]
            print(f"[inference] Shaped by failure IDs: {', '.join(ids)}")
        else:
            print("[inference] No training pairs found for this checkpoint")

    else:
        print("[inference] No active checkpoint found. Run rebirth.sh first.")

if __name__ == "__main__":
    main()


