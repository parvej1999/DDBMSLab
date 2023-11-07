from django.shortcuts import render
from .models import  demoForm
# Create your views here.

def  demoview(request):
    data = demoForm.objects.all()
    context={
        "objects":data,
    }
    print(context)
    if(request.method == "POST"):
        fname = request.POST.get('firstName')
        lname = request.POST.get('lastName')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phnumber = request.POST.get('number')
        
        
        # print(fname, lname)
        # instance = demo.objects.create(firstName = fname, lastName = lname)
        # print(instance)
        # instance.save()
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
        
    return render(request, "index.html", context)