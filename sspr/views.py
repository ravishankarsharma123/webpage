from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html', )
   # return HttpResponse('this is  home page ')
def firstpage(request):
    return render(request,'index1.html', )

def secondpage(request):
    return render(request,'index2.html', )

def thirdpage(request):
    return render(request,'index3.html', )
 