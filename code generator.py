import random

code_store = []

num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
low_alpha_list = ['a', 'b', 'c', 'd', 'e', 'f']
up_alpha_list = ['A', 'B', 'C', 'D', 'E', 'F']

l1 = num_list + low_alpha_list
l2 = num_list + up_alpha_list

random.shuffle(l1)
random.shuffle(l2)

choise = [l1, l2]
ran_choise = random.choice(choise)

print('your password is:- ', end='')
for i in ran_choise:
    print(i, end='')
    #print(type(i))
print('')

z = str(input('pin:- '))
for j in z:
    code_store.append(j)

if code_store == ran_choise:
    print('okay')

else:
    print('wrong pass')