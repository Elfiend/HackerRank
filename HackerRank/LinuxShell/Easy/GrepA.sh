#!/bin/sh
#
# Usage:
# 	sh GrepA.sh < GrepA.txt
# or
# 	cat GrepA.txt | sh GrepA.sh

grep -iw -E 'the|that|then|those'
# grep -iw 'the\|that\|then\|those'
# grep -iw -e 'the' -e 'that' -e 'then' -e 'those'
