
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view),
    path('signup/',views.Signup_page),
    path('login/',views.login_page),
    

]
