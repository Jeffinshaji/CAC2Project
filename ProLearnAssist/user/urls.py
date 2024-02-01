from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('Login' , views.user_login , name="Login"),
    path('courses',views.courses, name="course"),
    path('register' , views.user_register , name="user_register"),
    path('success',views.success,name='success'),
    path('userprofile',views.user_profile,name='userprofile'),
    path('logout',views.user_logout,name='logout'),
    path('lists',views.lists,name="lists"),
    path('useredit',views.user_edit,name="useredit")
    
]