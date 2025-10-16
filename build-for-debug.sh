#!/bin/bash

# set variables
PROJECT_DIR=$(pwd)

# install dependencies
sudo apt-get install -y python3 python3-pip
pip3 install -r requirements.txt

# install
cd PROJECT_DIR/
pip3 install -e .