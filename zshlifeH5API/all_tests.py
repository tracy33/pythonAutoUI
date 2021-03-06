# coding=utf-8
import unittest,time,os
import HTMLTestRunner #引入HTMLTestRunner包
#把public目录添加到path下，这里用的相对路径
#import send_mail
import sys
sys.path.append(".\\test_case\\public")
import send_mail,zshlogin


#引用公共变量--start
import globalcookie
logindata=open(".\\test_case\\public\\data.txt",'r')
un=''
pw=''
line=logindata.readline()
un,pw=line.split(',')
un=un.strip('\t\r\n')
pw=pw.strip('\t\r\n')
count=0
globalcookie.cookiestr="start"
while globalcookie.cookiestr=="start":
	count+=1
	if count>3:
		break
	globalcookie.cookiestr=zshlogin.login(un,pw)
	time.sleep(5)
	#print ("cookie:%s,运行次数 %d" %(globalcookie.cookiestr,count))
	continue
#end

if globalcookie.cookiestr!="start":
	listaa='.\\test_case'
	def createsuitel():
		testunit=unittest.TestSuite()
		#discover方法定义
		discover=unittest.defaultTestLoader.discover(listaa,
			pattern='start_*.py',
			top_level_dir=None)

		#discover方法筛选出来的用例，循环添加到测试套件中去
		for test_suite in discover:
			for test_case in test_suite:
				testunit.addTest(test_case)
				print testunit
		return testunit

	alltestnames=createsuitel()

	#定义个报告存放路径，支持相对路径。
	#filename='..\\report\\result2.html'
	#把测试报告结果文件根据生成时间命名
	#取前面时间
	now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
	#把当前时间加到报告中
	filename=".\\report\\"+now+'result.html'
	fp=file(filename,'wb')

	fp2=file('css.tpl','r')
	tmpxml=fp2.read()
	fp2.close()


	runner=HTMLTestRunner.HTMLTestRunner(
			stream=fp,
			title=u"最生活H5-API自动化测试报告",
			description=u"用例执行情况："
			)

	runner.STYLESHEET_TMPL=tmpxml
	runner.run(alltestnames)
	fp.close()
	# 些等待时间发现还是会最后一个套件不出报告,需要关闭文件才可以正常发送报告
	# mail_subject=u"最生活H5-API自动化测试报告"
	# send_mail.sendreport(".\\report",mail_subject)

else:
	now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
	f=open('.\\report\\'+now+'loginfail.html','wb')
	message="""
	<html>
	<head><strong>标题：</strong>登录失败时不运行接口用例，发送登录失败邮件</head>
	<body>
	<p><strong>运行结果：</strong>社区登录失败，已循环尝试3次登录，登录失败后将不会运行后续的接口用例</p>
	</body>
	</html>
	"""
	f.write(message)
	f.close()
	# print count
mail_subject=u"最生活H5-API自动化测试报告"
send_mail.sendreport(".\\report",mail_subject)
