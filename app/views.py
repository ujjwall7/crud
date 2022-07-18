from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def InsertPageView(request):
    return render(request,"app/insert.html")


def InsertData(request):
    # Data come from HTML to View
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    # Creating Object of Model Class
    # Inserting Data into Table
    newuser = Student.objects.create(Firstname=fname,Lastname=lname,    
                                        Email=email,Contact=contact)

    # After Insert render on Show.html
    # return render(request,"app/show.html")
    return redirect('show')



def read(request):
    # Reading Data from Table
    data = Student.objects.all()
    # Rendering Data on Show.html
    return render(request,"app/show.html",{'data':data})


def update(request,id):
    # Reading Data from Table
    data = Student.objects.get(id=id)
    # Rendering Data on Update.html
    return render(request,"app/edit.html",{'data':data})



#save

def save(request,id):
    udata=Student.objects.get(id=id)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']

    udata.save()

    return redirect('show') 


def delete(request,id):
    ddata=Student.objects.get(id=id)
    ddata.delete()
    return redirect('show')

    