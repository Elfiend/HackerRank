#!/bin/sh
#
# Usage:
# 	sh Awk3.sh < Awk.txt
# or
# 	cat Awk.txt | sh Awk3.sh

awk '{{sum = 0 ;sum += $2 + $3 +$4} if(sum>=240) {print $0,": A"} else if(sum>=180){print $0,": B"}else if(sum>=150){print $0,": C"}else {print $0,": FAIL"} }'
