count=1
for file in $(ls -U img|  grep -v / | head -n 20000)
do
  temp='img/'
  #echo $file
  #echo $temp$count
  mv $file $temp$count
  count=`expr $count + 1`
done
