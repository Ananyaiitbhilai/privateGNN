#!/bin/bash

# Loop through the 10 commands
for i in {1..10}
do
    # Run the Python command and append the output to the file
    python train.py gap-ndp --dataset reddit --epsilon 8 --encoder-epochs $i --epochs $i >> output_reddit.txt
done
