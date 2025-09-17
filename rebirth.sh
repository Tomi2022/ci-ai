#!/usr/bin/env bash
set -euo pipefail

# Detect Python across platforms
if [[ "$OS" == "Windows_NT" ]]; then
  # Hardcoded path for Windows (adjust if needed)
  PYTHON="/c/Users/Administrator/AppData/Local/Programs/Python/Python313/python.exe"
elif command -v python3 &>/dev/null; then
  PYTHON=python3
elif command -v python &>/dev/null; then
  PYTHON=python
else
  echo "ERROR: Python not found on this system."
  exit 1
fi

BASE=""
SINCE=""
OUTDIR="runs/rebirth_$(date +%Y%m%d_%H%M%S)"
DATA_PAIRS="$OUTDIR/train_pairs.jsonl"
CHECKPOINT_OUT="$OUTDIR/checkpoint"

while [[ $# -gt 0 ]]; do
  case $1 in
    --base) BASE="$2"; shift 2;;
    --since) SINCE="$2"; shift 2;;
    --outdir) OUTDIR="$2"; shift 2;;
    *) echo "Unknown arg: $1"; exit 1;;
  esac
done

mkdir -p "$OUTDIR"

echo "[0/5] Validating JSONL failures"
"$PYTHON" scripts/validate_jsonl.py "data/failures/failures_${SINCE//-/}.jsonl" || true

echo "[1/5] Gathering failures since $SINCE"
"$PYTHON" scripts/gather_failures.py --since "$SINCE" --out "$OUTDIR/failures_batch.jsonl"

echo "[2/5] Building contrastive pairs"
"$PYTHON" scripts/make_contrastive_pairs.py "$OUTDIR/failures_batch.jsonl" --out "$DATA_PAIRS"

echo "[3/5] Training DPO on $BASE"
"$PYTHON" scripts/train_dpo.py --base "$BASE" --data "$DATA_PAIRS" --out "$CHECKPOINT_OUT"

echo "[4/5] Evaluating checkpoint"
"$PYTHON" scripts/run_eval.py --checkpoint "$CHECKPOINT_OUT" --report "$OUTDIR/eval_report.json"

echo "[5/5] Promoting if gates pass"
"$PYTHON" scripts/promote_checkpoint.py --checkpoint "$CHECKPOINT_OUT" --report "$OUTDIR/eval_report.json"

echo "Done: $OUTDIR"
