#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

db=MySQLdb.Connect(host="localhost",user="root",password="satheesh29",database="hcm")
cur=db.cursor()
#cur.execute("use hcm")
#cur.execute("create table pdt2(p_name varchar(12),age int(3),dob DATE,m_status varchar(12),gender varchar(7),p_h int(3),p_w int(3),p_email varchar(30),address varchar(20),illness varchar(30),o_illness varchar(30))")


'''import cgi
form=cgi.FieldStorage()

p_name=form.getvalue("n")
age=form.getvalue("a")
dob=form.getvalue("d")
m_status=form.getvalue("ms1")
gender=form.getvalue("g")
p_h=form.getvalue("h")
p_w=form.getvalue("w")
p_email=form.getvalue("e")
p_add=form.getvalue("add")
ill=form.getvalue("ill")
o_ill=form.getvalue("oi")

query="insert into pdt2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=[p_name,age,dob,m_status,gender,p_h,p_w,p_email,p_add,ill,o_ill]
cur.execute(query,val)
db.commit()'''

cur.execute("SELECT * FROM pdt2")
result = cur.fetchall()

print('''
<html>
<style>
body{
background-image:url('imgp.jpg');
background-repeat:no-repeat;
background-size:cover;}
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
  color: white;
}

li {
  float: right;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #FF0000;
}
#st1
{
position:absolute;
height:600px;
width:400px;
margin-left:360px;
margin-top:30px;



}
</style>
<body>

<ul>
  <li><a class="active" href="home.py">Home</a></li>
  <li><a href="hcm.html">log out</a></li>
  <li><a href="about.py">About</a></li>
  <li><a href="patient_details.py">+ Add Patient </a></li>
  <br>
    Contact Us : +91 9345067935
</ul>
</body>
</html>
''')
print('''<html>''')
for row in result:
    print('''<br>''')
    print('''<label>PATIENT NAME :</label>''')
    print(row[0])
    print('''<br>''')
    print('''<br>''')
    print('''<label>AGE:</label>''')
    print(row[1])

    print('''<label style="margin-left:37px;">DOB :</label >''')
    print(row[2])
    print('''<label style="margin-left:37px;">STATUS :</label>''')
    print(row[3])
    print('''<br>''')
    print('''<br>''')
    print('''<label>HEIGHT :</label>''')
    print(row[5])
    print('''<label style="margin-left:37px;">WEIGHT :</label>''')
    print(row[6])
    print('''<br>''')
    print('''<br>''')
    print('''<label>EMAIL:</label>''')
    print(row[7])
    print('''<br>''')
    print('''<br>''')
    print('''<label>ADDRESS :</label>''')
    print(row[8])
    print('''<br>''')
    print('''<br>''')
    print('''<form action="mail.py">
    <label class="ls">Mail to</label>
    <input type="email" name="em" >
    <select name="ms1" id=ms"  style="margin-left:97px;">
    <option value="time to take medicine">time to take medicine</option>
    <option value="time to see docter">time to see docter</option>
    <option value="you medicine renewal time">you medicine renewal time</option>
    <option value="have good day">have good day</option>
    </select>
    <input type="submit" value="NOTIFY" style="margin-left:37px;"></form>''')
    print('''<br>''')

    print('''<label>----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</label>''')
    print('''<br>''')



print('''</html>''')

