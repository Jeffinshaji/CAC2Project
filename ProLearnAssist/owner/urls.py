from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.owner_login , name="ownerlogin"),
    path('homepage',views.dashboard,name="home"),
    path('alerts', views.alerts , name="alerts"),
    path('buttons', views.buttons , name="btn"),
    # path('card', views.card , name="card"),
    # path('forms', views.forms , name="forms"),
    # path('typography', views.typography , name="typography"),
    path('usertable',views.user_table, name="usertable"),
    path('statuschange/<int:id>',views.status_change,name="statuschange"),
    path('userdelete/<int:id>',views.user_delete,name="userdelete"),
    path('logout',views.owner_logout,name="Logout"),
    path('profile',views.profile,name="profile"),
    path('edit',views.profile_edit,name="edit"),
    path('user',include('user.urls')),
    
]