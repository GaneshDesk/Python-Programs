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

