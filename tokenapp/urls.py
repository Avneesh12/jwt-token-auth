from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("stu",Student_viewset,basename="student View")


urlpatterns = [
    path('hello/', HelloView.as_view(), name ='hello'), 
    path('stuviewset',include(router.urls)),
    path('blacklisttoken',logout_view)
]
