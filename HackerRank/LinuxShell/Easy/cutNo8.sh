while read usrInput
do
  echo "$usrInput" | cut -d ' ' -f 1-3
done
