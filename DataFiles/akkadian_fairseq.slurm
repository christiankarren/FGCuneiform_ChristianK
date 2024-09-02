#!/bin/sh

#SBATCH --job-name=akkadian_0.1_8000
#SBATCH --output=out
#SBATCH --error=err
#SBATCH --partition=studentkillable
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gpus=4

../akkadian_fairseq.sh result.LR_0.1.MAX_TOKENS_8000 0.1 8000

