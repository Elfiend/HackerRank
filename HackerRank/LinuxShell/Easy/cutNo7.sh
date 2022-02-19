while read usrInput
do
  echo "$usrInput" | cut -d ' ' -f 4
done
