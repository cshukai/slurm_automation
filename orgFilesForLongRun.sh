count=1
for file in $(ls -U | head -n 20000)
do
  temp='img/'
  mv $file $temp$count
  count=`expr $count + 1`
done
