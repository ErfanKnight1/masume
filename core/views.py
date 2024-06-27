from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from core.models import Customer,Profile, Messages, Resume
from core.forms import RegistraionForm,LoginForm,CustomerForm,ProfileForm
from django.contrib.auth import login as auth_login

from django.shortcuts import redirect


def home(request):
    customer_list=Customer.objects.all()
    user = request.user.is_authenticated

    usr = User.objects.get(id=1)

    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        text=request.POST.get("text")

        Customer.objects.create(name=name,phone=phone,email=email,text=text, user=usr)
    

    return render(request, "core/home.html",{"form":CustomerForm, 'auth':user})
    

def about(request):
    return render(request,"core/about.html")


def service(request):
    return render(request,"core/service.html")


def contact(request):
 
    return render(request,"core/contact.html")


def register(request):
    if request.method == "POST":
        print(request.POST)
        user_name = request.POST.get("username")
        # email = request.POST.get("email")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")

        user_obj = User.objects.filter(username=user_name).exists()

        if not user_obj:
            if password == repeat_password:
                User.objects.create(username=user_name, password=password)
                print('USER CREATED')
                return HttpResponseRedirect('/login')

    return render(request, "core/register.html", {"form": RegistraionForm})

def login(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("password")

        user_existance = User.objects.filter(username=username).exists()

        if user_existance:
            user_obj = User.objects.get(username=username)
            if user_obj.password == password:
                auth_login(request, user_obj)
                return HttpResponseRedirect('/resume')

    return render(request, "core/login.html", {"form": LoginForm})


def job(request):
    return render(request,"core/job.html")



def resume(request):
    user = request.user.is_authenticated
    
    if request.method=="POST":
        Resume.objects.create(
            user = request.user,
            name = request.POST.get('name'),
            phone_number = request.POST.get('phone'),
            age = request.POST.get('age'),
            coop_type = request.POST.get('type'),
            more_details = request.POST.get('text')
        )

    return render(request,"core/resume.html", context={'auth':user})

def profile(request):  
    profile_list=Profile.objects.all()

    print(request.user)

    tickets_list = Messages.objects.filter(user=request.user).values('id', 'user', 'user__username', 'DateandTime', 'message', 'answer')

    user = request.user.is_authenticated

    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        text=request.POST.get("text")

        Messages.objects.create(
            user = request.user,
            message = text
        )

        # profile.objects.create(name=name,phone=phone,email=email,text=text)

    return render(request,"core/profile.html",{"form":ProfileForm, 'auth':user, 'tickets_list':tickets_list})