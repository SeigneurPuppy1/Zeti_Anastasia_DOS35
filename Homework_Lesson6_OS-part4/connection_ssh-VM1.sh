#!/bin/bash


sudo ssh-keygen -t rsa -b 4096 -f /home/nastya/ssh-keys/id_rsa -P '2'
sudo ssh-copy-id -p 22 -i /home/nastya/ssh-keys/id_rsa.pub anastasia@192.168.203.131
