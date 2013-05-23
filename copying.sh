#!/bin/bash

# This function copies both to TEST and STAGE
# PREV file

#
# This is a newer version of a solaris script.
# 
#


# $1 is first argument
# $2 is second argument

FILENAME="$1"
# echo "$FILENAME"
DIR=src
if [ "X$2" != "X" ] 
	then
	  DIR="$2"
fi

# Do the TEST one to PREV first

if [ -e ../../dir1/shtdocs/$DIR/$FILENAME ]
  then
     cp -pf ../../dir1/shtdocs/$DIR/$FILENAME ../../dir1/shtdocs/$DIR/${FILENAME}.PREV
fi

# COPY TO TEST
cp -pf $DIR/$FILENAME ../../dir1/shtdocs/$DIR

# COPY TO STAGE -not working talk to Mark!
# cp -pf $DIR/$FILENAME ../../dir2/shtdocs/$DIR