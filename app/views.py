from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Tasks
from django.http import JsonResponse
# Create your views here.

  
def home(request): 
    Alltasks=Tasks.objects.all()
    tasks=[task for task in Alltasks if task.user==request.user]
    return render(request, 'app/index.html',{'Tasks':tasks})

def add_Task(request):
    if request.method=='GET':
        task=request.GET.get('task')
        deadline=request.GET.get('deadline')
        T=Tasks(user=request.user,task=task,deadline=deadline)
        T.save()
        return redirect('/')
    else:
        messages.error(request,"There is something wrong")
        return redirect('/')
    
def delete_Task(request):
    try:
        if request.method=='GET':        
            pk=request.GET.get('pk')
            task=Tasks.objects.get(sno=pk)
            task.delete()
            # task.is_active = False
            # task.save()
            response = JsonResponse({'message': 'data is deleted successfully'})
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            return response
 
    except Exception as e:
        print(e)
        return JsonResponse({'message': 'Internal Server Error'}, status=500)
def signUpHand(request):
    if request.method=='GET':
        name=request.GET.get('Name')
        
        username=request.GET.get('username')
        email=request.GET.get('email')
        password=request.GET.get('password')
        if  User.objects.filter(username=username).exists() :
            messages.error(request,'This username is taken')
            return redirect ('/')
        
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            login(request,user)
            messages.success(request,'Your account is created succefuly!!')
            return render(request, 'app\index.html')
            
    else:
        return redirect('/') 

def loginHand(request):
    if request.method=="GET":
        username=request.GET.get('username')
        password=request.GET.get('password')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"Username or Password is incorrect")
            
            return render(request, 'app\index.html')
        else:
            user.save()
            login(request,user)
            messages.success(request,"Successfully Logged In")
            # return render(request, 'app\index.html')
            return redirect('/')
        
def logoutHand(request):
    logout(request)
    messages.success(request,'Successfuly logout ')
    return redirect('/')