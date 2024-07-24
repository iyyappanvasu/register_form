from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas
# Create your views here.

def home(request):
  my_data=Datas.objects.all()
  if my_data:
    return render(request,"home.html",{'datas':my_data})
  else:
    return render(request,"home.html")

def add_data(request):
  if request.method == "POST":
    name=request.POST["name"]
    age=request.POST["age"]
    address=request.POST["address"]
    contact=request.POST["contact"]
    mail=request.POST["mail"]
    db=Datas(Name=name,Age=age,Address=address,Contact=contact,Mail=mail)
    db.save()
    return redirect ('home')
  return render(request,"home.html")


def update_data(request,id):
  my_data=Datas.objects.get(id=id)
  if request.method == "POST":
    name=request.POST["name"]
    age=request.POST["age"]
    address=request.POST["address"]
    contact=request.POST["contact"]
    mail=request.POST["mail"]
    my_data.Name=name
    my_data.Age=age
    my_data.Address=address
    my_data.Contact=contact
    my_data.Mail=mail
    my_data.save()
    return redirect('home')
  return render(request,"update.html",{'data':my_data})
  
def delete_data(request,id):
  my_data=Datas.objects.get(id=id)
  my_data.delete()
  return redirect('home')