#!/bin/bash

file=/var/users

create_user() {

sudo groupadd "$group"   2>/dev/null

#Sudoers
if [ "$group" = it ] || [ "$group" = security ]; then
   if ! grep -Fqw "%${group}" /etc/sudoers
   then
       sudo cp /etc/sudoers{,.bkp}
       echo "%$group ALL=(ALL) ALL" >> /etc/sudoers         
   fi
   
elif [ "$user" = admin ]; then
   if ! grep -Fqw "%${user}" /etc/sudoers
   then
       sudo cp /etc/sudoers{,.bkp}
       echo "$user  ALL=(ALL) ALL" >> /etc/sudoers          
   fi
   
fi

mkdir -v /home/anastasia/"$group"
sudo useradd "$user" -g "$group" -b /home/anastasia/"$group"

}


IFS=$'\n'

for line in $(cat $file)
do
    user=$(echo $line | cut -d' ' -f1)
    group=$(echo $line | cut -d' ' -f2)
    echo Username: "$user" Group: "$group"
    create_user
done
IFS=$oldIFS
