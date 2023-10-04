from django.urls import path
from remainder.views import SignUpView,SignInView,IndexView



urlpatterns=[

    path("signup",SignUpView.as_view(),name="signup"),
    path("signin",SignInView.as_view(),name="signin"),
    path("index",IndexView.as_view(),name="index")


    


]