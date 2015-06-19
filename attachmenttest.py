
import smtplib
import os
from email.mime.text import MIMEText
import time
import socket
from email.mime.multipart import MIMEMultipart

def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

sender = 'lixijin@richinfo.cn'  
receiver = 'liseau@qq.com'  
subject = 'python email test'  
smtpserver = 'smtp.richinfo.cn'  
username = 'lixijin'  
password = '1q2w3e'
hostname=os.getenv('computername')
   
msg=MIMEMultipart()
att1=MIMEText(open('/home/igvita-desert.reg').read(),'base64','gb2312')
att1["Content-Type"]='application/octet-stream'
att1["Content-Disposition"]='attachment;filename="igvita-desert.reg"'

# msg = '<html><h1>hello</h1>'+'<p>Form '+str(hostname)+'  '+str(socket.gethostbyname(socket.gethostname()))+'</p>'+'<p>'+str(GetNowTime())+'</p>'+'</html>','html','utf-8'
msg.attach(att1)
  
msg['Subject'] = subject
msg['From']="Xijin"+'<'+sender+'>'
msg['To']=receiver+";"

#print(msg)
smtp = smtplib.SMTP()
smtp.set_debuglevel(False)
smtp.connect('smtp.richinfo.cn')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit() 
