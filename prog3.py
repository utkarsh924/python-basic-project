# login program and indentation
# email-> us0304619@gmail.com
# password-> utkarsh19

email= input('Entered email')
password =input('Entered password')

if email=='us0304619@gmail.com' and password=='1234':
 print('welcome on your insta account')
elif email=='us0304619@gmail.com' and password !='1234':
 # Tell the user
 print('incorrect password')
 password=input('entered the password again')
 if password=='1234' :
  print('Welcome,Finally!')
 else:
  print('Beta tumse naa ho paega')
else:
 print('not correct')



