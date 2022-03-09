#!/bin/sh
#
# Usage:
# 	sh LonelyInteger.sh < LonelyInteger.txt
# or
# 	cat LonelyInteger.txt | sh LonelyInteger.sh

read n
read pairs

#echo "${pairs}" | tr -s ' ' '\n' | sort | uniq -c | grep '^[ ]*[1]' | awk '{print $2}'
echo "${pairs}" | tr -s ' ' '\n' | sort | uniq -u
