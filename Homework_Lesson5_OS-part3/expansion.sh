#!/usr/bin/env bash

#Проверяю, что введено два парметра
if [ $# -ne 2 ]; then
   echo "Error"
   exit 1
fi

#Задаю переменные
filename=$1
new_filename=$2

#Удаляем расширение файла, если расширения нет, то имя не поменяется
new_expansion="${filename%.*}.$new_filename"

#Переименование файла
mv "$filename" "$new_expansion"

echo "Файл $filename переименован $new_expansion"
