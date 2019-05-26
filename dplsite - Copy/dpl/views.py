from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"newhome.html")

def blr1(request):
    return render(request,"newteams.html")

def blr1pg2(request):
    return render(request,"blr1pg2.html")

def blr2(request):
    return render(request,"blr2.html")

def blr2pg2(request):
    return render(request,"blr2pg2.html")

def blr2pg3(request):
    return render(request,"blr2pg3.html")

def schedules(request):
    return render(request,"index.html")

def hyd(request):
    return render(request,"hyd.html")

def fun(request):
    return render(request,"newstat.html")

def spa_pointstableblr1(request):
    return render(request,"spa_pointstableblr1.html")

def spa_pointstableblr2(request):
    return render(request,"spa_pointstableblr2.html")

def spa_pointstablehyd(request):
    return render(request,"spa_pointstablehyd.html")

def show(request):
    return render(request,"newhome.html")
