# `rebirth.sh`


```bash


#!/usr/bin/env bash
set -euo pipefail


# Rebirth pipeline (skeleton)
# Usage: ./rebirth.sh --base base-v0 --since 2025-09-01 --outdir runs/rebirth_$(date +%Y%m%d_%H%M)


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


echo "[1/5] Gathering failures since $SINCE"
python3 scripts/gather_failures.py --since "$SINCE" --out "$OUTDIR/failures_batch.jsonl"


echo "[2/5] Building contrastive pairs"
python3 scripts/make_contrastive_pairs.py "$OUTDIR/failures_batch.jsonl" --out "$DATA_PAIRS"


echo "[3/5] Training DPO on $BASE"
python3 scripts/train_dpo.py --base "$BASE" --data "$DATA_PAIRS" --out "$CHECKPOINT_OUT"


echo "[4/5] Evaluating checkpoint"
python3 scripts/run_eval.py --checkpoint "$CHECKPOINT_OUT" --report "$OUTDIR/eval_report.json"


echo "[5/5] Promoting if gates pass"
python3 scripts/promote_checkpoint.py --checkpoint "$CHECKPOINT_OUT" --report "$OUTDIR/eval_report.json"


echo "Done: $OUTDIR"