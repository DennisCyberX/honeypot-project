#!/bin/bash
echo "Setting up the honeypot..."
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install --upgrade pip
echo "Dependencies installed."
echo "To start the honeypot, run: python3 scripts/honeypot.py"
