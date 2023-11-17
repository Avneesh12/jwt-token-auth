from django.shortcuts import render

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated 
from rest_framework import viewsets

from stu.models import Student
from stu.serializerr import Studentserializer

from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
  
  
class HelloView(APIView): 
    permission_classes = (IsAuthenticated, ) 
  
    def get(self, request):
        stu = Student.objects.all()
        ser = Studentserializer(stu,many=True)  
        return Response(data=ser.data) 
    
    def post(self,request):
        stu = Studentserializer(data=request.data)
        if stu.is_valid():
            stu.save()
            return Response(data={"res":"Student Added"})
        else:
            return Response(data={"res":stu.errors})
        


class Student_viewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, ) 
    queryset = Student.objects.all()
    serializer_class = Studentserializer



@api_view(['POST'])
def logout_view(request):
    ref_token = request.data['refresh']
    token = RefreshToken(ref_token)
    token.blacklist()
    return Response(data={"res":"Logout Success"})