from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User, UserImage
from functions import handle_uploaded_file 

import jwt, datetime
# Create your views here.
def homepage(request):
    try:
        token = request.COOKIES.get("jwt")
        payload = jwt.decode(token,'secret',algorithms=['HS256']) 
    except:
        if(request.method=="GET"):
            return render(request, "homepage.html",{})
        else:
            return redirect(login)
    else:
        user = User.objects.filter(id = payload["id"]).first()
        us = UserImage.objects.filter(u1 = user)
        if(user.user == 'Admin'):
            u1 = UserImage.objects.all()
            return render(request, "dashboard.html",{"user" : user,"u1":u1})
        elif(user.user == 'Teacher'):
            u2 = User.objects.filter(user = "Student")
            list1 = []
            for i in u2:
                u2 = UserImage.objects.filter(u1 = i.id)
                return render(request, "dashboard.html",{"user" : user,"u1":u2,"us":us})
        else:
            return render(request, "dashboard.html",{"user" : user,"u1" : us})
def login(request):
    if(request.method == "GET"):
        return render(request,"login.html",{})
    else:
        password = request.POST["password"]
        email =request.POST["email"]
        try:
            user= User.objects.get(email = email,password = password)
        except:
            return redirect(homepage)
        else:
            payload = {
            "id":user.id,
            "exp": datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
            }
            token = jwt.encode(payload,'secret',algorithm="HS256")
            resp = redirect(homepage)
            resp.set_cookie(key= "jwt",value=token,httponly= True)
            return resp

def dashboard(request):
    id = request.POST["user"]
    u2 = User.objects.get(id=id)
    data = u2.user + "/" + u2.email + "/"
    handle_uploaded_file(request.FILES['file'], data)
    file = request.FILES["file"]
    u1 = UserImage()
    u1.u1 = u2
    u1.image = file
    u1.save()
    return redirect(homepage)


def logout(request):
    response = redirect(homepage)
    response.delete_cookie("jwt")
    return response

def register(request):
    if(request.method=="GET"):
        return render(request,"register.html",{})
    else:
        name = request.POST["name"]
        email =request.POST["email"]
        phone = request.POST["phone"]
        password= request.POST["password"]
        user = request.POST["user"]
        try:
            user = User.objects.get(email = email)
        except:
            u1 = User()
            u1.name = name
            u1.email = email
            u1.phone = phone
            u1.password = password
            u1.user = user
            u1.save()
            return HttpResponse("<center> <h2>  Register Successfully. </h2> <a href='/'> homepage </a>  </center> ")
        return HttpResponse("<center> <h2> Email Already Exist.</h2>  <a href='/'> homepage </a> </center> ")