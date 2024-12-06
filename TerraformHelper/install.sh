#!/bin/bash
#
############################################################################
#
# Author : Sahil
# Date   : 06/12/2024
#
# version: v1
#
# This Script is to Insatall Terraform on Ubuntu / Linux
#
#############################################################################
#

set -e
set -u

echo "Running Installation of Terrafrom"
echo
echo "Updating Software Properties"
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

echo "Installing Hashicorp GPG Keys"
wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

echo "Verifying Finger Print"
gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint

echo "Add the official HashiCorp repository to your system. The lsb_release -cs command finds the distribution release codename for your current system, such as buster, groovy, or sid."

echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list

echo "Running Updation"
sudo apt update > /dev/null

echo "Installing Terraform"
sudo apt-get install terraform -y

echo "Verying Installation"
terraform -version
