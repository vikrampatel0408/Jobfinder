from django.shortcuts import render
from django.shortcuts import (get_list_or_404,
                              HttpResponseRedirect)

# from .models import jobseeker
# from .forms import JobseekerForm

# def create_view (request):
#     context ={}
#     form=JobseekerForm(request.POST or None)

#     if form.is_valid():
#         form.save()

#     context['form']=form
#     return render(request,"job_seeker_create.html",context)

def home_view(request):
    return render(request,"index.html")
def Signup_page(request):
    return render(request,"signup.html")
def login_page(request):
    return render(request, "login.html")