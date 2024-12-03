#!/bin/bash
#
set -u
echo "select which script to execute"
echo "------------------------------------"
ls | grep ".py"
echo
echo "------------------------------------"
 read -p "Enter name of script : " script

 echo "Executing $script.py "
 sleep 5s
 python "$script.py"
sleep 5s
