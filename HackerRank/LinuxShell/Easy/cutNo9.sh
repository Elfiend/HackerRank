while read usrInput
do
  echo "$usrInput" | cut -d $'\t' -f 2-
done
