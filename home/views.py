from django.shortcuts import render
from home.models import Contact

def home(request):
    return render(request,'base.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def project(request):
    return render(request, 'projects.html')
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        desc=request.POST['desc']
        ins=Contact(name=name,email=email,desc=desc)
        ins.save()
        print("data is written in database")
    return render(request,'contact.html')