#!/usr/bin/env bash

function executeTest() {
	project=$1
	if [ ! -e ${project}.py ]; then
		echo "$project is not exist."
		return
	fi

	echo "${project} Excutes."
	python3 ${project}.py <${project}.txt
}

function chooseDifficulty() {
	PS3="Choose the test Difficulty: "
	ProjectsDirs=(
		"exit"
		$(ls -d */)
	)
	select projectDir in ${ProjectsDirs[@]}; do

		if [ "$projectDir" == "exit" ]; then
			exit 0
		fi
		if [ ! -d "$projectDir" ]; then
			echo "$projectDir is not a folder."
			continue
		fi

		break
	done
}

function chooseProject() {
	PS3="Choose the test project: "
	projects=(
		"exit"
		".."
		$(ls -t ${projectDir}*.py | sed 's/\.py//g')
	)
	select project in ${projects[@]}; do
		case $project in
		exit)
			exit 0
			;;
		..)
			break
			;;
		*)
			executeTest ${project}
			;;
		esac
	done
}

export OUTPUT_PATH=$(pwd)/output.txt

while :; do
	chooseDifficulty
	chooseProject
done
