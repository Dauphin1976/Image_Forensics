#!/bin/bash
# since Bash v4

# Run All Algorithms.
# **************************

# Run ELA Algorithms.
cd Algorithms/ela
python demo.py

# Run CopyMoveDetection Algorithms.
cd ../copy-move-detection/CopyMoveDetection
python main_CLI.py

# Run perceptualHash Algorithms.
cd ../../perceptualHash
python perceptualHash.py ph1.jpg ph1copie.jpg
python perceptualHash.py ph1.jpg ph2.jpg
python perceptualHash.py ph1.jpg ph3.jpg
