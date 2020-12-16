import random
import smtplib

# function defined to send mails
def sendmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'password')
    server.sendmail('your email id', to, content)
    server.close()

'''flag = 0
tryList = ['a', 's', 'd', 'f']
random.shuffle(tryList)
newStr = ''.join(tryList)
print(newStr)'''

# code_store = []

num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
low_alpha_list = ['a', 'b', 'c', 'd', 'e', 'f']
up_alpha_list = ['A', 'B', 'C', 'D', 'E', 'F']

l1 = num_list + low_alpha_list
l2 = num_list + up_alpha_list

random.shuffle(l1)
random.shuffle(l2)

choise = [l1, l2]
ran_choise = random.choice(choise)

code = ''.join(ran_choise)
# print('code:-', code)

try:
    content = code
    to = 'your email id'  # you can use multiple mail id(s) using and statement
    sendmail(to, content)
    print('your new code code has been sent to your mail...')
except Exception as e:
    print(e)
    print("i'm not able to send the code...")

'''print('your password is:- ', end='')
for i in ran_choise:
    print(i, end='')
    #print(type(i))
print('')'''

z = str(input('pin:- '))
if z == code:
    print('okay')

else:
    print('wrong')
'''for j in z:
    code_store.append(j)

if code_store == ran_choise:
    print('okay')

else:
    print('wrong pass')'''