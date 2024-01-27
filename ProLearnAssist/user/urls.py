from django.urls import path
from user import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('login' , views.user_login , name="login"),
    path('courses',views.courses, name="course"),
    path('register' , views.user_register , name="user_register"),
    path('success',views.success,name='success'),
    path('userprofile',views.user_profile,name='userprofile'),
    
]