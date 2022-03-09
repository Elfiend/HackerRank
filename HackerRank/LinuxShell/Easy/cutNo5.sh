while read usrInput
do
  echo "$usrInput" | cut -d $'\t' -f 1-3
done
