#!/bin/bash

RUNDIR="/modelrun"
OUTDIR="/output"

data_file=$1
model_file=$2

data_file_name=$(basename "$data_file")
model_file_name=$(basename "$model_file")

if [[ ! -d $RUNDIR ]]; then
  mkdir $RUNDIR
fi
if [[ ! -d $OUTDIR ]]; then
  mkdir $OUTDIR
fi

cd $OUTDIR

python3 /clews_ethiopia_model/preprocess_data.py "$data_file" "$RUNDIR/$data_file_name" "$model_file" "$RUNDIR/$model_file_name"
glpsol --check -m "$RUNDIR/$model_file_name" -d "$RUNDIR/$data_file_name" --wlp "$RUNDIR/lpfile.lp"
cbc "$RUNDIR/lpfile.lp" solve -solu "$OUTDIR/combined_results.txt"
python3  /clews_ethiopia_model/postprocess_data.py "$OUTDIR/combined_results.txt" "$OUTDIR"
