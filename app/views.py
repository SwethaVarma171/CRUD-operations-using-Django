from django.shortcuts import render,redirect
from .models import Game
data=Game.objects.all()
game={
    'data':data
}
def display(request):
    return render(request,'index.html',game)
def details(request,pk):
    data1=Game.objects.get(id=pk)
    if request.method=="POST":
        data1.delete()
        return redirect('home')
    context={
        'data1':data1
    }
    return render(request,'single_details.html',context)

def update(request,jp):
    update=True
    data2=Game.objects.get(id=jp)
    if request.method == "POST":
        name=request.POST.get('name')
        place=request.POST.get('place')
        thing=request.POST.get('thing')
        number=request.POST.get('number')
        print(name,place,thing,number)
        data2.name=name
        data2.place=place
        data2.thing=thing
        data2.number=number
        data2.save()
        return redirect('home')
        # print(name,place,thing,number)
    context={
        'data2':data2,
        'update':update
    }
    return render(request,'edit.html',context)
def create(request):
    update=False
    if request.method == "POST":
        name=request.POST.get('name')
        place=request.POST.get('place')
        thing=request.POST.get('thing')
        number=request.POST.get('number')
        print(name,place,thing,number)
        a=Game.objects.create(name=name,place=place,thing=thing,number=number)
        return redirect("home")
    return render(request,'add.html',{'update':update})
