from django.shortcuts import render, redirect
from .models import  demoForm
# Create your views here.

def  demoview(request):
    data = demoForm.objects.all()
    context={
        "objects":data,
    }
    print(context)
    if(request.method == "POST"):
        if request.POST.get("create") == "create":
            fname = request.POST.get('firstName')
            lname = request.POST.get('lastName')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            password = request.POST.get('password')
            phnumber = request.POST.get('number')
            
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
            email = request.POST.get("email")
            password = request.POST.get("password")
            phnumber = request.POST.get("number")
            print(fName)
            # instance.save()
            instance.update(
                firstName = fName, 
                lastName = lName,
                email = email,
                password = password,
                phnumber = phnumber
            )
            
        
    return render(request, "index.html", context)

    
