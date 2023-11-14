import random
from formapp.models import  demoForm

fname = open("/home/parvej/Desktop/ddbmsLabProject/DDBMSLab/formapp/fnames.txt", 'r')
# print(fname)
lname = open('formapp/lnames.txt', 'r')
fnames = []
lnames = []
for i in fname:
    name = i.split("\n")
    fnames.append(name[0])
for i in lname:
    name = i.split("\n")
    lnames.append(name[0])

# print(len(fnames))
gen = ['Male', "Female", 'Others']

for i in range(1000):
    fname = fnames[random.randint(0, (len(fnames)-1))]
    lname = lnames[random.randint(0, (len(lnames)-1))]
    email = fname+lname+"@gmail.com"
    gender = gen[random.randint(0, 2)]
    password = ''
    number = None
    for i in range(11):
        if i<=5:
            password += chr(random.randint(97,123))
        else:
            password += str(random.randint(0,9))
        number = random.randint(100000000,999999999)
    print(fname, lname, email, gender, password, number)
    instance = demoForm.objects.create(firstName = fname, lastName = lname, gender=gender, email = email, password = password, phnumber = number, createTime=datetime.datetime.now())


