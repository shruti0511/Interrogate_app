from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path("sign_up/",views.SignupUSER,name="SignupUSER"),
    path("",views.LoginUSER,name="LoginUSER"),
    path("log_out/",views.LogoutUSER,name="LogoutUSER"),
    path("profile/",views.ProfileUSER,name="ProfileUSER"),
    path("topics/",views.topics,name="topics"),
    path("changeProfile/",views.changeProfile,name="changeProfile"),
    path("delAns<int:sno>/",views.deleteAns,name="deleteAns"),
    path("delQue<int:sno>/",views.deleteQue,name="deleteQue"),
    path("<str:username>/",views.othersProfile,name="othersProfile"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

