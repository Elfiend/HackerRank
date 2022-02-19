while read usrInput
do
  echo $(cut -c 3 <<< $usrInput)
done
