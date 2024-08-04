from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime,timedelta
from django.contrib.auth.decorators import login_required

# from .forms import userform 
# Create your views here.

@login_required(login_url='login')
def student(request):
    data={
        'title':'website',
        'clist':['sidharth','prashant','prateek'],
        'numbers':[1,2,3,45,6],
        'data_details':[
        {'name':'pradeep','lastname':'sidharth','phonenumber':123456},
        {'name':'pradeep','lastname':'sidharth','phonenumber':123456},
         {'name':'pradeep','lastname':'sidharth','phonenumber':123456},
          {'name':'pradeep','lastname':'sidharth','phonenumber':123546},
    ]
    }

    
    return render(request,"students.html",data)

# def aboutus(request,about):
#     return HttpResponse("welcome to about us page ")

from django.shortcuts import render, redirect

def login(request):
    if request.method == "POST":
        n3 = request.POST.get("username")
        n4 = request.POST.get("password")
        if n3 == "login" and n4 == "123456":
            return render(request, "students.html")
        else:
            data1 = {"error": "Invalid username or password"}
            return render(request, "login.html", data1)
    return render(request, "login.html")


def userform(request):
    final_result=0
    data={}
    try :
        n1=int(request.GET["num1"])
        n2=int(request.GET["num2"])
        final_result=n1+n2
        data={
            "n1":n1,
            "n2":n2,
            "output":final_result
        }

    except:
        pass
    return render(request,"formget.html",data)

def userform2(request):
    final_result=0
    data1={}
    try :
        if request.method=="post":
            n3=int(request.POST["num3"])
            n4=int(request.POST["num4"])
            final_result=n1+n1
        data1={
            "n3":n3,
            "n4":n4,
            "output1":final_result,
        }
    except:
        pass
    return render(request,"formPost.html",data1)


from django.contrib.auth.decorators import login_required

def calculator(request):
    data12={}
    d=""
    try:
        if request.method =="POST":
            
            n11=eval(request.POST.get("num11"))
            n22=eval(request.POST.get("num22"))
            opr= request.POST.get("opr")
            if opr=="/":
                d=n11/n22
            elif opr=="+":
                d=n11+n22
            elif opr=="-":
                d=n11-n22
            elif opr=="*":
                d=n11*n22
            data12={

                "n11":n11,
                "n22":n22,
                "dat":d
            }
    except:
        d="invalid operator......"
    return render(request,"calculator.html",data12)

def show_current_time(request):
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d this is time : %H:%M:%S")
    return HttpResponse(f"<h1>The current date : {formatted_time} </h1>")

def show_time_ahead_before(request):
    now = datetime.now()
    time_ahead=now+timedelta(hours=4)
    time_before=now-timedelta(hours=4)
   
    return HttpResponse(f"<h2> {time_ahead} and other one {time_before} </h1>")

def fruitss(request):
    fruitss={
        "fruits": ['apple','orange','banana',],
        "student":['sidharth','sidram','sneha','preeti']
    }
    return render(request,"fruits.html",fruitss)

    