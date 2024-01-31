from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

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
    return render(request, 'owner/main/alerts.html')
def user_table(request):
    data=User.objects.all()
    return render(request, 'owner/main/usertable.html',{"data":data})
def learner_table(request):
    return render(request, 'owner/main/learnertable.html')
def tutor_table(request):
    return render(request, 'owner/main/tutortable.html')
def subject_table(request):
    return render(request,'owner/main/subjecttable.html')
def profile(request):
    return render(request,'owner/main/ownerprofile.html')
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
    

