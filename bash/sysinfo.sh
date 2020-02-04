#!/bin/bash
#this script will email us our username, IP, hostname and today's date.
emailaddress=jpick6@gmail.com
content="$USER"
today=$(date +"%D %T")
bash=$BASH_VERSION
ip=$(ip a | grep 'dynamic ens192' | awk '{print $2}')
mail -s "IT3038C Linux IP" $emailaddress <<<$(echo -e "User" $content "from IP" $ip "on" $today "with hostname" $HOSTNAME "running" $bash "version of bash")
