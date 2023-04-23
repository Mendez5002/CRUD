from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def Home(request):
     data = Student.objects.all()
     Context= {'data': data}
     return  render(request , 'index.html')

def edit(request):
     return render(request,'edit.html')
def login(request):
     return render(request , 'login.html')

def InsertData(request,id):
     if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          age = request.POST.get('age')
          gender = request.POST.get('gender')

          query = Student(name=name, email=email, age=age, gender=gender)
          query.save()
          return render("/")

     return render(request, 'index.html')


def updateData(request, id):
     if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          age = request.POST.get('age')
          gender = request.POST.get('gender')

          edit = Student.objects.get(id=id)
          edit.name = name
          edit.email = email
          edit.gender = gender
          edit.age = age
          edit.save()
          return redirect("/")

     d = Student.objects.get(id=id)
     context = {"d": d}
     return render(request, "edit.html", context)


def deleteData(request, id):
     d = Student.objects.get(id=id)
     d.delete()
     return redirect("/")

     return render(request, "index.html")


def handlelogin(request):
     if request.method == "POST":
          username = request.POST.get("username")
          password = request.POST.get("password")
          myuser = authenticate(username=username, password=password)

          if myuser is not None:
               login(request, myuser)
               return redirect('/')

          else:
               return redirect('/login')

     return render(request, 'login.html')


def handlesignup(request):
     if request.method == "POST":
          username = request.POST.get("username")
          password = request.POST.get("password")
          myuser = User.objects.create_user(username, password)
          myuser.save()

     return render(request, 'signup.html')


def handlelogout(request):
     logout(request)
     return redirect('/signup')



