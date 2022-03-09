#!/bin/sh
#
# Usage:
# 	sh Awk1.sh < Awk1.txt
# or
# 	cat Awk1.txt | sh Awk1.sh

awk '{ if (NF < 4) {print "Not all scores are available for",$1}}'
