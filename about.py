#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")
print('''
<html>
<style>
body{
background-image:url('img2.jpg');
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
p{
font-size:30px
font-family:"Lucida Console"
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
  <li><a href="hcm.html">Home</a></li>
  <li><a href="signup.py">sign up</a></li>
  <li><a href="login.py">log in</a></li>
  <li><a class="active" href="about.py">About</a></li>
  <br>
    Contact Us : +91 9345067935
</ul>
<p style="color:white" >
<b>HEALTH CARE MANAGEMENT</b><br>
The motive of this app is to set reminder to the older people to take medicines on time.
This includes , the people should set notification or alarm to take medicines,
to see doctor on time and maintain medicine count also.
So that, it will help them to take care of themselves without depending on others.</p>
</body>
</html>
''')
