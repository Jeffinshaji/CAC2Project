from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from user.models import User,user_details,interests


@login_required(login_url='ownerlogin')
def dashboard(request):
    return render(request , 'owner/main/dashboard.html')
def buttons(request):
    return render(request, 'owner/main/buttons.html')
# def card(request):
#     return render(request, 'owner/main/card.html')
# def forms(request):
#     return render(request, 'owner/main/forms.html')
# def typography(request):
#     return render(request, 'owner/main/typography.html')
def alerts(request):
    data = interests.objects.all()
    return render(request, 'owner/main/alerts.html',{'data':data})
def user_table(request):
    data=User.objects.all()
    return render(request, 'owner/main/usertable.html',{"data":data})
def learner_table(request):
    learner=User.objects.filter(is_staff=False)
    return render(request, 'owner/main/learnertable.html',{'learner':learner})
def tutor_table(request):
    tutor=User.objects.filter(is_staff=True,is_superuser=False)
    accepted=interests.objects.filter(Teaching_status=2)
    return render(request, 'owner/main/tutortable.html',{'tutor':tutor,'accepted':accepted})
def subject_table(request):
    return render(request,'owner/main/subjecttable.html')
def profile(request):
    data = user_details.objects.get(user=request.user)
    return render(request,'owner/main/ownerprofile.html',{'data':data})
def profile_edit(request):
    return render(request,'owner/main/owneredit.html')

def owner_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
        if user is not None and user.is_superuser==True :
            login(request , user)
            return render(request , 'owner/main/dashboard.html')
        elif user is None:
            msg = "Wrong credentials. Please try again!"
            return render(request , 'owner/main/login.html' , {'msg':msg})
    return render(request , 'owner/main/login.html')

def owner_logout(request):
    logout(request)
    return redirect('ownerlogin')

def status_change(request,id):
    user=User.objects.get(id=id)
    if user.is_active==True:
        user.is_active=False
    else:
        user.is_active=True
    user.save()
    return redirect("usertable")

def user_delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect("usertable")

def teaching_change(request,id):
    interest = interests.objects.get(id = id)
    if interest.Teaching_status == 2:
        interest.Teaching_status = 1
    elif interest.Teaching_status == 1:
        interest.Teaching_status = 2

    interest.save()
    return redirect('alerts')


    

