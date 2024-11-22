from django.http import HttpResponse
from django.shortcuts import render, redirect

from . models import movie
from . forms import movieform

# Create your views here.
def index(request):
    obj=movie.objects.all()
    result={
        'movie_list':obj
    }
    return render(request,'index.html', result)

def details(request,movie_id):
    obj=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'result':obj})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        year=request.POST.get("year")
        image=request.FILES["image"]
        result=movie(name=name,description=description,year=year,image=image)
        result.save()
        return redirect('/')
    return render(request,'add.html')


def update(request,id):
    mov=movie.objects.get(id=id)
    form1=movieform(request.POST or None, request.FILES,instance=mov)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'modify.html',{'mov':mov,'form1':form1})

def delete(request,id):
    if request.method=="POST":
        movie1=movie.objects.get(id=id)
        movie1.delete()
        return redirect('/')
    return render(request,'delete.html')
