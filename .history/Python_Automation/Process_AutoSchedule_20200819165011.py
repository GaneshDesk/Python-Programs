# Automation script which accepts time interval from user and create log file in that
# Marvellous directory which contains information of all running processes.
# After creating the log file send that log file through mail.

import os 
import time
import psutil
import urllib2
import smtplib
import schedule