#!/bin/bash
#--------------------------------------------------------------

#  SBATCH CONFIG
#-----------------------------------------------
#SBATCH --job-name=gpu_test                # name for the job
#SBATCH --cpus-per-task=1                  # number of cores
#SBATCH --time 0-02:00                     
#SBATCH --partition Gpu
#SBATCH --mem=20G
#---------------------------
# env
source activate
module load  cuda/cuda-10.0.130
module load cudnn/cudnn-7.4.2-cuda-10.0.130
export HDF5_USE_FILE_LOCKING='FALSE'

#https://github.com/qqwweee/keras-yolo3/issues/443
#https://github.com/experiencor/keras-yolo3
