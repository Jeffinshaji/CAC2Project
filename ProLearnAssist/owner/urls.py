from django.urls import path
from . import views

urlpatterns = [
    path('', views.owner_login , name="dashboard"),
    path('homepage',views.dashboard,name="home"),
    path('alerts', views.alerts , name="alerts"),
    path('buttons', views.buttons , name="btn"),
    path('card', views.card , name="card"),
    path('forms', views.forms , name="forms"),
    path('typography', views.typography , name="typography"),
    path('usertable',views.user_table, name="usertable"),
    path('statuschange/<int:id>',views.status_change,name="statuschange"),
    path('userdelete/<int:id>',views.user_delete,name="userdelete"),
    
]