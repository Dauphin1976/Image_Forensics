#!/bin/bash
# since Bash v4

# Run setup to install all requirements.
# **************************

sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo apt-get update
sudo pip install Pillow
sudo pip install -U scikit-learn
sudo pip install tqdm
python -m pip install --user scipy numpy matplotlib ipython jupyter pandas sympy nose
