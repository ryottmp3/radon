#!/bin/bash

# This script will create new data directories

echo Listing Current Directories:
ls -d */

echo " "
echo "Do you need to make a single new directory or a range of new directories? (single/range): " 
read sinRan
echo " "

if [ $sinRan == "single" ] || [ $sinRan == "Single" ]
then 
	echo "You need a single diectory."
	echo "What Run Number is the Directory? (int) "
	read runNum
	echo "Making directory Run0$runNum "
	mkdir Run0$runNum
	mkdir Run0$runNum/A
	echo "Done. "
elif [ $sinRan == "range" ] || [ $sinRan == "Range" ]
then
	echo "You need a range of directories. "
	echo "Enter the lower bound of the range: "
	read low
	echo "Enter the upper bound of the range: "
	read high
	echo "The range you need is from $low to $high."
	echo "Creating directories in the range ($low $high)... "
	for (( num = $low ; num <= $high ; num++ ));
	do
		echo "Creating directory Run_$num and subdirectories. "
		mkdir Run0$num
		mkdir Run0$num/A
	done
	echo "Done. "
else
	echo "Invalid Input. "
fi

echo " "
echo "New list of directories: "
ls -d */

