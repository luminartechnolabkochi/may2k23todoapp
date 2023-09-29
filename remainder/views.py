from django.shortcuts import render,redirect
from remainder.forms import RegistrationForm
from django.views.generic import View
from django.contrib import messages


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
        
            # User.objects.create_user(**form.cleaned_data)


