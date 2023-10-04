from django.shortcuts import render,redirect
from remainder.forms import RegistrationForm,LoginForm
from django.views.generic import View
from django.contrib import messages
# model relation ship
# 1:1 1:M M:M



class SignUpView(View):
    
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration completed successfully")
            return redirect("signup")
        else:
            messages.error(request,"faild to create account")
            return render(request,"signup.html",{"form":form})
        


class SignInView(View):

    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    





