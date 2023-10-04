from django.shortcuts import render,redirect
from remainder.forms import RegistrationForm,LoginForm
from django.views.generic import View,TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
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
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)   
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("signin")
            else:
                messages.error(request,"invalid credentials!!!")
                return render(request,"login.html",{"form":form})
            
class IndexView(TemplateView):

    template_name="index.html"

    







