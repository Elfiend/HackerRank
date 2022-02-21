#!/bin/bash
#
# Usage:
# 	bash FunctionsandFractals.sh < FunctionsandFractals.txt
# or
# 	cat FunctionsandFractals.txt | bash FunctionsandFractals.sh

declare -A maps
readonly rows=62
readonly columns=99

readonly baseX=49
readonly baseY=62
readonly baseFractal=16

readonly space='_'
readonly tree='1'

function initMaps() {
	for i in $(seq 0 $rows); do
		for j in $(seq 0 $columns); do
			maps[$i, $j]=$space
		done
	done
}

function treeGrow() {
	local center_x=$1
	local center_y=$2
	local growFractal=$3
	local growTimes=$4

	local left_x
	local right_x

	# Trunk
	for i in $(seq 1 $growFractal); do
		maps[$center_y, $center_x]=$tree
		center_y=$((center_y - 1))
	done

	# Branch
	for i in $(seq 1 $growFractal); do
		left_x=$((center_x - i))
		maps[$center_y, $left_x]=$tree
		right_x=$((center_x + i))
		maps[$center_y, $right_x]=$tree
		center_y=$((center_y - 1))
	done

	if [ "$growTimes" -gt 1 ]; then
		growFractal=$((growFractal / 2))
		growTimes=$((growTimes - 1))

		treeGrow $left_x $center_y $growFractal $growTimes
		treeGrow $right_x $center_y $growFractal $growTimes
	fi

}

function printIteration() {
	for i in $(seq 0 $rows); do
		for j in $(seq 0 $columns); do
			printf "%s" "${maps[$i, $j]}"
		done
		echo
	done
}

initMaps
read usrInput
treeGrow $baseX $baseY $baseFractal $usrInput
printIteration
