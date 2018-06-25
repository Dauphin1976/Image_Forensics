#!/bin/bash
# since Bash v4

# Run perceptualHash Algorithm.
# **************************

# Run demo perceptualHash Algorithms.
cd Algorithms/perceptualHash
python -m perceptualHash ph1.jpg
python -m perceptualHash --format=decimal ph1.jpg
python -m perceptualHash --format=matrix ph1.jpg
python perceptualHash.py ph1.jpg ph1copie.jpg
python perceptualHash.py ph1.jpg ph2.jpg
python perceptualHash.py ph1.jpg ph3.jpg
