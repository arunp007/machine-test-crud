from django.shortcuts import render,redirect
from.models import *

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        logindetails = Login(username = username, password = password)
        logindetails.save()

    return render(request, 'login.html')

def logintable(request):
    infodetails = Login.objects.all()
    return render(request, 'logintable.html', {'info': infodetails})       

def admin(request):
    return render(request, 'adminpage.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        detail = Registration1(name = name, contact = contact, email = email, username = username, password = password, cpassword = cpassword)
        detail.save()

    return render(request, 'registration.html')

def regtable(request):
    studentsinfo = Registration1.objects.all()
    return render(request, 'registrationtable.html', {'info': studentsinfo})

def update(request,id):
    updatedata = ""
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        Registration1.objects.filter(id=id).update(name=name,contact=contact,email=email,username=username,password=password,cpassword=cpassword)
        return redirect('regtable')
    
    else:
        updatedata = Registration1.objects.get(id=id)
        return render(request, 'registration.html', {'update' : updatedata})


    








