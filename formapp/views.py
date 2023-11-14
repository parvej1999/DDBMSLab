from django.shortcuts import render, redirect
from .models import  demoForm
import random, datetime
# Create your views here.


def  demoview(request):
    data = demoForm.objects.all().order_by("-createTime")
    context={
        "objects":data,
    }
    print(context)
    if(request.method == "POST"):
        if request.POST.get("create") == "create":
            fname = request.POST.get('firstName')
            lname = request.POST.get('lastName')
            gender = request.POST.get('gender').capitalize()
            email = request.POST.get('mail')
            password = request.POST.get('pass')
            phnumber = request.POST.get('num')
            
            instance = demoForm.objects.create(
                firstName = fname, 
                lastName = lname,
                gender = gender,
                email = email,
                password = password,
                phnumber = phnumber
                )
            instance.save()
            
            print(request.POST)
            print("Form Saved")
        
        if request.POST.get("delete") == "delete":
            print('___________delete________________')
            id = request.POST.get("instance_id")
            instance = demoForm.objects.filter(id = id)
            print("instance with id ",id, " got deleted")
            instance.delete()
        
        if request.POST.get("update") == "update":
            print('___________update________________')
            id = request.POST.get("update_id")
            instance = demoForm.objects.filter(id = id)
            print(id)
            print("instance with id ",id, " got updated")
            fName = request.POST.get("fname")
            lName = request.POST.get("lname")
            email = request.POST.get("mail")
            password = request.POST.get("pass")
            phnumber = request.POST.get("num")
            print(fName)
            # instance.save()
            instance.update(
                firstName = fName, 
                lastName = lName,
                email = email,
                password = password,
                phnumber = phnumber
            )
            
        return redirect("form")
    return render(request, "index.html", context)

def bulkDataEntry(request):
    data = demoForm.objects.all().order_by("createTime")
    context={
        "objects":data,
    }
    fname = open("formapp/extraFiles/fnames.txt", 'r')
    # print(fname)
    lname = open('formapp/extraFiles/lnames.txt', 'r')
    fnames = []
    lnames = []
    for i in fname:
        name = i.split("\n")
        fnames.append(name[0])
    for i in lname:
        name = i.split("\n")
        lnames.append(name[0])

    fname.close()
    fname.close()

    # print(len(fnames))
    gen = ['Male', "Female", 'Others']

    for i in range(100):
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
        # print(fname, lname, email, gender, password, number)
        instance = demoForm.objects.create(firstName = fname, lastName = lname, gender=gender, email = email, password = password, phnumber = number, createTime=datetime.datetime.now())
    # return render(request, "index.html", context)
    return redirect("form")

def bulkDataDelete(request):
    instances = demoForm.objects.all()
    for i in instances:
        i.delete()
    return redirect("form")
