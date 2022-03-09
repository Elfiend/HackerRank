while read usrInput
do
  echo $usrInput | cut -c 2,7
  #echo "${usrInput:1:1}""${usrInput:6:1}"
done
