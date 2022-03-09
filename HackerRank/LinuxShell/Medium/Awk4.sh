#!/bin/sh
#
# Usage:
# 	sh Awk4.sh < Awk.txt
# or
# 	cat Awk.txt | sh Awk4.sh

# paste -d';' - -
# awk 'ORS=NR%2?";":"\n"'
awk 'BEGIN {ORS = ""} {if(NR%2){print $0";"}else{print $0"\n" } }'
