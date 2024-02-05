from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from .models import user_details, interests, improvements,teching,feedback
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


# def feedbackform(request):
#     if request.method == 'POST':
#         name=request.POST["name"]
#         print(name)
#         Date=request.POST["date"]
#         print(Date)
#         Instructor=request.POST["instructor"]
#         print(Instructor)
#         Content=request.POST["Content"]
#         print(Content)
#         level=request.POST["tutorlevel"]
#         print(level)
#         material=request.POST["Material"]
#         print(material)
#         Turating=request.POST["rating"]
#         print(Turating)
#         allrating=request.POST["overall"]
#         print(allrating)
#         comment=request.POST["comments"]
#         print(comment)
#         Feedback=feedback.objects.create(name=name, Date=Date,Instructor=Instructor,Content=Content,levelofteaching=level, Material=material,Rating=Turating, Overallrating=allrating,Comments=comment)
#         Feedback.save()
#         return redirect('Thanks')
            
    # return render(request, 'user/main/register.html')
        # return render(request, 'user/main/thanks.html')
    
    # else:
    #     object = feedback()
    return render(request, 'user/main/feedback.html')


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

def lists(request,sub):
    tlist=interests.objects.filter(Subject=sub,Teaching_status=2)
    tstatus = teching.objects.filter(teach_to=request.user)
    a = []
    return render(request,"user/main/list.html",{'tlist':tlist,'status':a})

def user_feedback(request):
    if request.method == 'POST':
        user_id=request.user.id
        user=User.objects.get(id=user_id)
        name=request.POST["uname"]
        print(name)
        Date=request.POST["date"]
        print(Date)
        Instructor=request.POST["iname"]
        print(Instructor)
        Content=request.POST["content"]
        print(Content)
        level=request.POST["tulevel"]
        print(level)
        material=request.POST["material"]
        print(material)
        Turating=request.POST["rating"]
        print(Turating)
        allrating=request.POST["Overall"]
        print(allrating)
        comment=request.POST["msg"]
        print(comment)
        Feedback=feedback.objects.create(user=user,name=name, Date=Date,Instructor=Instructor,Content=Content,levelofteaching=level, Material=material,Rating=Turating, Overallrating=allrating,Comments=comment)
        Feedback.save()
        return redirect('thanks') 
    else:
        return render(request,"user/main/feedback.html")
    
def thanks(request):
    return render(request,'user/main/thanks.html')

def user_edit(request):
    
    if request.method=='POST':
        
        Subject=request.POST['interest']
        improve=request.POST['improvements']
        
        #Teaching=request.POST['']
        interest=interests.objects.create(user=request.user,Subject=Subject)
        interest.save()
        improvement=improvements.objects.create(user=request.user,Learning=improve)
        improvement.save()

        return render(request,"user/main/edit.html")

    
    data = user_details.objects.filter(user_id = request.user)
    return render(request,"user/main/edit.html",{'data':data})

def teach_noti(request,id):
    interest = interests.objects.get(id=id)
    interest.Teaching_status = 1
    interest.save()
    return redirect('userprofile')


    
def change(request,id):
    user =User.objects.get(id=id)
    if teching.objects.filter(teach_by=user,teach_to=request.user,teach_status=0).exists():
        teach = teching.objects.get(teach_by=user,teach_to=request.user,teach_status=0)
        teach.teach_status = 1
        teach.save()
    else:
        teach = teching.objects.create(teach_by=user,teach_to=request.user)
    return redirect('userprofile')

