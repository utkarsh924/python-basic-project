# Extract username from a given email
# eg if the email is us0304619@gmail.com
# then username should be us0304619

user= input('Enter the email:')

pos= user.index('@')
print(user[0:pos])