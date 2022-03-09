#!/bin/sh
#
# Usage:
# 	sh GrepB.sh < GrepB.txt
# or
# 	cat GrepB.txt | sh GrepB.sh

grep '\(\d\) *\1\+'
# grep '\([0-9]\) *\1\+'
# grep -E '([[:digit:]])[[:space:]]*\1+'
