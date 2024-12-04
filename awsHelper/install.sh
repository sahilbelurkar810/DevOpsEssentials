#!/bin/bash

###########################################################################
#
# Author : Sahil
# Date   : 04/12/24
#
# Version : v1
#
# This script installs AWS CLI on Ubuntu 24.
#
###########################################################################

set -e
set -u
echo "Updating and upgrading the system..."
sudo apt update && sudo apt upgrade -y

echo "Installing required dependencies..."
sudo apt install curl unzip -y

echo "Downloading AWS CLI..."
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

echo "Unzipping AWS CLI package..."
unzip awscliv2.zip

echo "Running AWS CLI installation..."
sudo ./aws/install

echo "Verifying AWS CLI installation..."
aws --version

echo "Cleaning up..."
rm -rf awscliv2.zip aws

echo "AWS CLI installation completed successfully!"

