#!/bin/bash

#Назначаю переменные

out_file=$1
dir=$2
expansion=$3

touch $out_file

if [ -d $dir  ]; then

  ls $dir |  grep $expansion > $out_file 2>&1

else

   echo "not a directory"

fi

