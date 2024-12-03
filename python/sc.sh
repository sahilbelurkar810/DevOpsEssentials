#!/bin/bash
#set -x
set -u
#echo "i am working"
#ls | grep -v "temp" >> pythos
#cat pythos
for file in *.py;do
	echo "Executing the $file...."
	python "$file"
	echo "done executing $file.py"
	echo "____________________________________________________________________________"
	echo
	sleep 5s
done
