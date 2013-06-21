#database
import os
import sqlite3
conn = sqlite3.connect('afterh2t.db')
c = conn.cursor()
#c.execute('''CREATE TABLE data
#			  (rollno text, dob text, name text, mothername text, fathername text, category text, subcategory text, statecode text, physics #num, chemistry num, maths num, total num, boardrollno text, year text, board text)''')
#search and find
for fil in os.listdir("/home/ig/Desktop/projectjm/pdata/"):
	print fil
	f = open("/home/ig/Desktop/projectjm/pdata/"+fil).read()
	roll_no_text_pos = f.find("Roll No")
	roll_no = f[roll_no_text_pos+14:roll_no_text_pos+14+8]
	print roll_no
	dob_text_pos = f.find("DOB",roll_no_text_pos)
	dob = f[dob_text_pos+11:dob_text_pos+11+10]
	print dob
	name_text_pos = f.find("Name",dob_text_pos)
	name = f[name_text_pos+11:f.find("**",name_text_pos+11)]
	print name
	mname_text_pos = f.find("Mother",name_text_pos)
	mname = f[mname_text_pos+20:f.find("**",mname_text_pos+20)]
	print mname
	fname_text_pos = f.find("Father",mname_text_pos)
	fname = f[fname_text_pos+20:f.find("**",fname_text_pos+20)]
	print fname
	cat_text_pos = f.find("Category",fname_text_pos)
	cat = f[cat_text_pos+26:f.find("Sub",cat_text_pos)]
	print cat
	subcat_text_pos = f.find("Sub",cat_text_pos)
	subcat = f[subcat_text_pos+19:f.find("**",subcat_text_pos+19)]
	print subcat
	scoe_text_pos = f.find("State",subcat_text_pos+19)
	scoe = f[scoe_text_pos+27:f.find("**",scoe_text_pos+27)]
	print scoe
	phy_text_pos = f.find("Physics",scoe_text_pos+27)
	phy = f[phy_text_pos+12:f.find("**",phy_text_pos+12)]
	print phy
	chem_text_pos = f.find("Chemistry",phy_text_pos+12)
	chem = f[chem_text_pos+14:f.find("**",chem_text_pos+14)]
	print chem
	math_text_pos = f.find("Math",chem_text_pos+14)
	math = f[math_text_pos+16:f.find("**",math_text_pos+16)]
	print math
	total_text_pos = f.find("Total",math_text_pos+16)
	total = f[total_text_pos+11:f.find("**",total_text_pos+11)]
	print total
	broll_text_pos = f.find("Roll",total_text_pos)
	broll = f[broll_text_pos+52:f.find("Year",broll_text_pos+52)-1]
	print broll
	yop_text_pos = f.find("Year",broll_text_pos+52)
	yop = f[yop_text_pos+18:yop_text_pos+18+4]
	print yop
	board_text_pos = f.find("Exam",yop_text_pos+18+4)
	board = f[board_text_pos+23:f.find("\n",board_text_pos+23)]
	print board
	c.execute("INSERT INTO data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",			(roll_no,dob,name,mname,fname,cat,subcat,scoe,phy,chem,math,total,broll,yop,board))
	conn.commit()
conn.close()
print "Done...Trying to fetch from database"








