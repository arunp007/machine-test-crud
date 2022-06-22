from msilib.schema import tables
from django.shortcuts import render,redirect
from.models import *

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            admin_details = Login.objects.get(username=username, password=password)
            request.session['xyz'] = admin_details.id
            return redirect('admin')

        except Login.DoesNotExist:
            return render(request, 'login.html', {'message': "Username And Password Is Wrong"}) 
    return render(request, 'login.html')

    
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
        return render(request, 'student_register.html', {'update' : updatedata})


def delete(request,id):
    Registration1.objects.get(id=id).delete()
    return redirect('regtable')

def student_register(request):
    return render(request, 'student_register.html')

def student_login(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        try:
            student_details = Registration1.objects.get(email=email, password=password)
            request.session['xyz'] = student_details.id
            return redirect('regtable')

        except Registration1.DoesNotExist:
            return render(request, 'login.html', {'message': "Username And Password Is Wrong"}) 
    return render(request, 'login.html')


def logout_admin(request):
    request.session.flush()
    return redirect('login')

def logout_student(request):
    request.session.flush()
    return redirect('student')


    








