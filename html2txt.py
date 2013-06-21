# Read data in html format and process into without tags data
# Html data from "data" and processed data into "pdata"
import html2text
h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True
for fil in os.listdir("/home/ig/Desktop/projectjm/data/"):
	print fil
	f = open("/home/ig/Desktop/projectjm/data/"+fil).read()
	w = open("/home/ig/Desktop/projectjm/pdata/"+fil,'w')
	w.write(h.handle(f))
	w.close()
	f.close()

