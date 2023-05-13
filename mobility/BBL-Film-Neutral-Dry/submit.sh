#!/bin/bash -l
#SBATCH -p batch 
#SBATCH -J ct-comp
#SBATCH -o job.out
#SBATCH -N 1
#SBATCH -n 16
#BATCH -w node1
#SBATCH -t 200:00:00

conda activate morphct

python -u kmc-script.py

