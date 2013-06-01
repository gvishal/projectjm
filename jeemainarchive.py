﻿import httplib2
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

