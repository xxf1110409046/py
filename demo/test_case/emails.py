import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

def sendEmails():
    msg_from = '1321872905@qq.com'  # 发送方邮箱
    msg_reciver = '"550490482"<550490482@qq.com>'  # 接收方邮箱
    code = 'jweqdafbtntlidee'  # 授权码

    subject = 'python测试邮箱'  # 主题
    content = '这就是小熊测试的python测试报告发送到邮箱的结果，希望的到好的反馈'  # 正文
    msg = MIMEMultipart()
    msg.attach(MIMEText(content))
    # 获取对象，封装信息
    msg['subject'] = Header("测试", 'UTF-8')
    msg['from'] = Header("小熊", 'utf-8')
    msg['to'] = msg_reciver

    # 构建附件句柄
    att1 = MIMEText(open('H:\HTMLTestReportCN.html', 'rb').read(), 'base64', 'UTF-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="test.html"'
    msg.attach(att1)
    try:
        print("授权码1")
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        print("授权码2")
        s.login(msg_from, code)
        print("授权码3")
        s.sendmail(msg_from, msg_reciver, msg.as_string())
        print("发送成功")
    except Exception:
        print(Exception.args)
    finally:
        s.quit()






