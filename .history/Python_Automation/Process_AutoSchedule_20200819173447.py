# Automation script which accepts time interval from user and create log file in that
# Marvellous directory which contains information of all running processes.
# After creating the log file send that log file through mail.

import os 
import time
import psutil
import urllib
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib.request.urlopen('www.google.com', timeout=1)
        return True
    except Exception as e:
        return False

def ProcessLog(log_dir = 'Marvellous'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    seperator="-"* 80
    log_path = os.path,join(log_dir,"Marvellous%s.log"%(time.ctime()))
    f = open(log_path,'w')
    f.write(seperator+"\n")
    f.write("Your Process Logger is : "+time.ctime()+"\n") 
    f.write(seperator+"\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms/(1024 * 1024)
            pinfo['vms']= vms
            listprocess.append(pinfo)

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass       
















