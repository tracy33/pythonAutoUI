# coding=utf-8
import os,time,datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header

#定义发送邮件
def sentmail(file_new,subje):
	smtpserver='smtp.exmail.qq.com'
	#发送信箱
	mail_from='tracytan@gdtengnan.com'

	#收信信箱
	mail_to='tracytan@gdtengnan.com'
	#mail_to='dycp_dev@gdtengnan.com'
	#用户名和密码
	un='tracytan@gdtengnan.com'
	pw='133@Gdqq'
	subject=subje
	#定义正文
	f=open(file_new,'rb')
	mail_body=f.read()
	#构造附件
	att_name=os.path.basename(file_new)
	att=MIMEText(mail_body,'base64','utf-8')
	att['Content-Type']='application/octet-stream'
	att['Content-Disposition']='attachment; filename='+att_name
	#att['Content-Disposition']='attachment; filename="report.html"'
	f.close()
	#msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
	#msg=MIMEText(mail_body,'html','utf-8')
	msg = MIMEMultipart('alternative')
	email_content=MIMEText(mail_body,'html','utf-8')
	'''
	只发送html格式邮件，邮件里不能运行js，所有无法展开报告的detail，现在选择的办法是即发送邮件html内容看大概，又构造附近可以以浏览器打开查看detail
	'''
	#定义标题
	msg['subject']=Header(subject,'utf-8')
	msg['From']=Header('自动化用例邮件','utf-8')
	msg.attach(email_content)
	msg.attach(att)
	#msg['Subject']=u'搜索登录测试报告'
	#定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
	#msg['date']=time.strftime('%a,%d %b %Y %H:%M:%S %z')

	#连接smtp服务器
	smtp=smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.login(un,pw)
	smtp.sendmail(mail_from,mail_to,msg.as_string())
	smtp.quit()

	print 'email has send out!'


#查找测试报告，调用发邮件功能
def sendreport(re_dir,subject):
	result_dir=re_dir
	#用于获取目录下的所有文件列表
	lists=os.listdir(result_dir) 
	#将获取到的文件根据文件创建时间排序
	lists.sort(key=lambda  fn:   os.path.getmtime(result_dir+"\\"+fn) if not  os.path.isdir(result_dir+"\\"+fn) else 0)
	print ('最新测试生成的报告为：'+lists[-1])

	#找到最新生成的文件。join()方法用来连接字符串，通过路径与文件名的拼接，我们将得到目录下最新被创建的的文件名的完整路径
	file=os.path.join(result_dir,lists[-1])
	print file

	#调用发邮件模块
	sentmail(file,subject)

'''
if __name__=="__main__":
	sendreport()
'''
