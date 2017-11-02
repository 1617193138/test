import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '18852278125@163.com'
msg['to'] = '813818992@qq.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('18852278125@163.com', 'jishuyuan')
smtp.sendmail('18852278125@163.com', '813818992@qq.com', str(msg))
smtp.quit()