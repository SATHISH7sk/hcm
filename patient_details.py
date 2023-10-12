#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi

print('''
<html><head>
<style>
body{
background-image:url('img3.jpg');
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

.l1
{
position:absolute;
height: 500px;
width: 500px;
background-color:pink;


}
</style></head>
<body>

<ul>
  <li><a href="home.py">Home</a></li>
  <li><a href="hcm.html">log out</a></li>
  <li><a href="about.py">About</a></li>
  <li><a class="active">+ Add Patient </a></li>
  <br>
    Contact Us : +91 9345067935
</ul>
<br><br>
<b><center>Patient Details Form</center><br><br>
<br><br>
<center><div class="l1">
<form  action="h.py">
<label class="ls">Patient Name:</label><input type="text" name="n" style="margin-left:37px;"><br><br>
<br>
<label class="ls">Age:</label><input type="number" name="a" style="margin-left:107px;"><br><br>
<br>
<label class="ls">DOB:</label><input type="date" name="d" style="margin-left:154px;"><br><br>
<br>
<label class="ls">Marital Status:</label>
<select name="ms1" id=ms"  style="margin-left:127px;">
  <option value="Single">Single</option>
  <option value="Married">Married</option>
  <option value="Divorsed">Divorsed</option>
  <option value="Widowed">Widowed</option>
  </select><br><br>
  <br>

<label class="ls">Gender :</label>
<input type="radio" name="g" value="1"> MALE
<input type="radio" name="g" value="1"> FEMALE
<input type="radio" name="g" value="0"> OTHERS<br><br>
<br>
<label class="ls">Patient Height:</label><input type="number" name="h" style="margin-left:37px;"><br><br>
<br>
<label class="ls">Patient Weight:</label><input type="number" name="w" style="margin-left:37px;"><br><br>
<br>
<label class="ls">Patient Email:</label><input type="email" name="e" style="margin-left:47px;"><br><br>
<br>
<label class="ls">Address:</label><input type="text" name="add" style="margin-left:87px;"><br><br>
<br>
<label class="ls">Illnesses:</label>
<select name="ill" id="il" style="margin-left:92px;">
  <option value="Asthma">Asthma</option>
  <option value="Other">Other</option>
  <option value="Cancer">Cancer</option>
  <option value="Diabetes">Diabetes</option>
  <option value="Emotienal Disoder">Emotienal Disoder</option>
  <option value="Heart Disease">Heart Disease</option>
  <option value="Heart Attack">Heart Attack</option>
  <option value="Fever">Fever</option>
  <option value="High Blood Pressure">High Blood Pressure</option>
  <option value="Digestive Problems">Digestive Problems</option>
  <option value="Ulcer">Ulcer</option>
  <option value="Kidney Disease">Kidney Disease</option>
  <option value="Lung Disease">Lung Disease</option>
  <option value="Sleep Apnea">Sleep Apnea</option>
  <option value="Thyroid Problems">Thyroid Problems</option>
  </select><br><br>
  <br>
<label class="ls">Other illnesses :</label><input type="text" name="oi"  style="margin-left:42px;"><br><br>
<br>
<label class="ls">Current Medicine :</label><input type="text" name="med" style="margin-left:22px;"><br><br></b>
<br>
<center><input type="submit" value="UPLOAD" style="background-color: #04AA6D;"><br><br></center>
</form>
</div></center>
</body>
</html>
''')
