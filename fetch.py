﻿import httplib2
from urllib import urlencode
h=httplib2.Http(cache=None)
url="http://cbseresults.nic.in/jee/jee13_cbse.asp"
headers={'Connection': 'keep-alive','Origin': 'http://cbseresults.nic.in','Referer': 'http://cbseresults.nic.in/jee/jee_cbse_2013.htm','Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'}
day=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
month=['01','02','03','04','05','06','07','08','09','10','11','12']
year=['1995','1994','1993','1992','1996']
loopsDone = False
regno = '82912021'
f = open("dob.txt",'w')
for cyear in year:
	if loopsDone:
		break
	for cmonth in month:
		if loopsDone:
			break
		for cday in day:
			dob = cday+'/'+cmonth+'/'+cyear
			data={'regno':regno,'dob':dob,'b2':'Submit'}
			f.write(dob)
			f.write('\n')
