from django.shortcuts import render

# Create your views here.


def killer(request):
    return render(request,'killer.html')



def devil(request):
    return render(request,'devil.html')