#!/bin/sh

read n

echo $n
total=0
for i in $(seq 0 $(($n-1)))
do
  read input
  echo $i $input $total
  echo "Result:$total"
  total=`expr $input + $total`
done

printf %.3f "$(bc -l <<< $total/$n)"
