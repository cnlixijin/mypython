import smtplib
import os
from email.mime.text import MIMEText
import time
import socket

def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

sender = 'liseau@qq.com'  
receiver = 'lixijin@richinfo.cn'  
subject = 'python email test'  
smtpserver = 'smtp.qq.com'  
username = 'liseau'  
password = 'fj1229'
hostname=os.getenv('computername')
   
msg = MIMEText('<html><h1>Hello</h1>'+'<p>Form '+str(hostname)+'  '+str(socket.gethostbyname(socket.gethostname()))+'</p>'+'<p>'+str(GetNowTime())+'</p>'+'</html>','html','utf-8')
  
msg['Subject'] = subject
msg['From']="Xijin"+'<'+sender+'>'
msg['To']=receiver+";"

#print(msg)
smtp = smtplib.SMTP()
smtp.set_debuglevel(False)
smtp.connect('smtp.qq.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit() 
