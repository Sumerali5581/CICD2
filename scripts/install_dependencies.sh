#!/bin/bash

# Update packages and resolve conflicts
sudo yum update --best --allowerasing -y

# Install Python 3 and pip
sudo yum install python3 -y
sudo yum install python3-pip -y

# Install Flask
pip3 install flask
