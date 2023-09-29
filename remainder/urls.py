from django.urls import path
from remainder.views import SignUpView



urlpatterns=[

    path("signup",SignUpView.as_view(),name="signup"),
    


]