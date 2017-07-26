from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Todos,Priority


# Create your views here.
def index(request):
    todos= Todos.objects.all()[:10]
    context={
        'todos':todos,
    }
    return  render(request,'index.html',context
)
def add(request):
   
    priorities=Priority.objects.all()[:3]
    context ={
        'priorities':priorities
    }
    
    if(request.method=='POST'):
        title=request.POST['title']
        text=request.POST['text']
        id=request.POST['priority']
        priority=Priority.objects.get(id=id)
        todo=Todos(title=title,text=text,priority=priority)
        todo.save()
        return redirect('/todos')
    else:
        return  render(request,'add.html',context)

def edit(request,id):
    priorities=Priority.objects.all()[:3]
    todo =Todos.objects.get(id=id)
    return  render(id,'add.html',{'priorities':priorities,'todo':todo})


def details(request,id):
    
    todo =Todos.objects.get(id=id)
    context ={
        'todo':todo,
      
    }
    return  render(request,'details.html',context)

def delid(request,id):
    
    try:
        data = { 'is_deleted':Todos.objects.filter(id=id).delete() }
    except Todos.DoesNotExist:
        if not data['is_deleted']:
            data['error_message'] = 'A user with this username already exists.'
           
    return JsonResponse(data)


