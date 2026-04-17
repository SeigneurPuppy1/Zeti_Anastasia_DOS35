#!/bin/bash

sudo ssh-keygen -t rsa -b 4096 -f /home/nastya/ssh-keys/id_rsa_host -P '2'
sudo ssh-copy-id -p 22 -i /home/nastya/ssh-keys/id_rsa_host.pub anastasia@172.29.190.204
