#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

def validate_jsonl(path: Path):
    if not path.exists():
        print(f"[ERROR] File not found: {path}")
        return False

    ok = True
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                json.loads(line)
            except json.JSONDecodeError as e:
                print(f"[ERROR] Invalid JSON at line {i}: {e}")
                print(f"  → {line[:80]}")
                ok = False
    if ok:
        print(f"[OK] {path} is valid JSONL.")
    return ok

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+", help="JSONL files to validate")
    args = ap.parse_args()

    all_ok = True
    for f in args.files:
        if not validate_jsonl(Path(f)):
            all_ok = False

    if not all_ok:
        sys.exit(1)

if __name__ == "__main__":
    main()
