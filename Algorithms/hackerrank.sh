#!/bin/sh

function executeTest()
{
	project=$1
	if [ ! -e ${project}.py ]
	then
		echo "$project is not exist."
		return
	fi

	python3 ${project}.py < ${project}.txt
}

export OUTPUT_PATH=$(pwd)/output.txt
PS3="Choose the test target: "
Projects=(
	"exit"
)

select project in ${Projects[@]}
do
	case $project in
	exit)
		break
	;;
	*)
		executeTest ${project}
	;;
	esac
done