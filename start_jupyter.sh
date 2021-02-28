#!/bin/bash
export PATH="/scratch/ovs72384/anaconda3/bin:$PATH"
source /scratch/ovs72384/anaconda3/bin/activate
conda activate cuda-slic
module load cuda/10.1
jupyter notebook --no-browser --port 8877
