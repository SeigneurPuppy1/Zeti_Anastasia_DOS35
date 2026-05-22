#!/bin/bash

create_user() {

#Sudoers
sudo groupadd "$group"   2>/dev/null

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

            mkdir -v "/home/anastasia/$group"
            useradd "$user" -g "$group" -b "/home/anastasia/$group"
            echo "User "$user" in group "$group" created successfully."
}

select option in "Add user" "Show users" "Exit"
do
    case $option in
        "Add user")
            read -rp "Enter username:"  user
            read -rp "Enter group:"  group
            create_user
            ;;
        "Show users")
            cut -d: -f1 /etc/passwd
            ;;
        "Exit")
            break
            ;;
        *)
            echo "Wrong option. Choose a number."
            ;;
    esac
done
