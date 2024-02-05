from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from .models import user_details, interests, improvements
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here.



def user_profile(request):
    data = user_details.objects.filter(user_id = request.user)
    interest=interests.objects.filter(user_id = request.user)
    improvement=improvements.objects.filter(user_id = request.user)
    return render(request,"user/main/userprofile.html",{'data':data,'interest':interest,'improvement':improvement})


def index(request):
    return render(request,"user/main/index.html")

def about(request):
    return render(request,"user/main/about.html")
def courses(request):
    return render(request,"user/main/courses.html")





# def user_login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username , password=password)
#         if user is not None and user.is_active:
#             if user.is_superuser==False and user.is_staff==False:
#                 login(request,user)
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            if user.is_superuser==False and user.is_staff==True:
                login(request,user)
                return redirect('userprofile')
            elif user.is_superuser==False and user.is_staff==False:
                login(request,user)
                return redirect('userprofile')
        elif user is None:
            msg = "Wrong credentials. Please try again!"
            return render(request , 'user/main/login.html' , {'msg':msg})
    return render(request , 'user/main/login.html')

def user_register(request):
    if request.method=='POST':
        username=request.POST['name']
        if User.objects.filter(username=username).exists():
            msg = 'username already exists!'
            return render(request, 'user/main/register.html',{'msg':msg})
        else:
            email=request.POST['email']
            password=request.POST['password']
            phone=request.POST['phone']
            qualification=request.POST['qualification']
            current=request.POST['current']
            institution=request.POST['institution']
            interest=request.POST['interest']
            new_password = make_password(password)
            if interest=='Tutor':
                a=True
            else:
                a=False
            User.objects.create(username=username,email=email,password=new_password,is_staff=a)
            user1=User.objects.filter(username=username,password=new_password,email=email)
            for i in user1:
                if i.username==username:
                    user=i.id
                    break
            user = User.objects.get(id=user)
            user_details.objects.create(user=user,Phone=phone,Qualification=qualification,Interest=interest,CurrentStatus=current,Institution=institution)
            return redirect('success')
            
    return render(request, 'user/main/register.html')
def success(request):
    return render(request,'user/main/success.html')

def user_logout(request):
    logout(request)
    return redirect('Login')

def lists(request):
    return render(request,"user/main/list.html")

def user_feedback(request):
    return render(request,"user/main/feedback.html")

def user_edit(request):
<<<<<<< HEAD
    data = user_details.objects.filter(user_id = request.user)
    return render(request,"user/main/edit.html",{'data':data})
    
=======
    
    if request.method=='POST':
        
        Subject=request.POST['interest']
        improve=request.POST['improvements']
        userid=request.POST['userid']
        
        #Teaching=request.POST['']
        interest=interests.objects.create(user=User.objects.get(id=userid),Subject=Subject)
        interest.save()
        improvement=improvements.objects.create(user=User.objects.get(id=userid),Learning=improve)
        improvement.save()

        return render(request,"user/main/edit.html")

    
    data = user_details.objects.filter(user_id = request.user)
    return render(request,"user/main/edit.html",{'data':data})


    

>>>>>>> 42413313de3d4db134c8c28be71fd0d85dcc4ff4
