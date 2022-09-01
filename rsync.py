# sshpass install
# rsync install

import os, sys, subprocess

GETVARPath = "sshpass -p 'My_Pass' rsync -zarvh -e 'ssh -p 22' root@My_IP_Server:"


pathALL = {
"/var/www/user/data/www/site.com/api":"/var/www/user/data/www/site.com",
"/var/www/user/data/www/site.com/tempfile":"/var/www/user/data/www/site.com",
"/var/www/user/data/www/site.com/MyCloud":"/var/www/user/data/www/site.com",
"/var/www/user/data/www/site.com/i":"/var/www/user/data/www/site.com"
}


for val in pathALL.keys():
    cmdRun = GETVARPath+val+" "+pathALL[val]
    subprocess.call(cmdRun, shell=True)
