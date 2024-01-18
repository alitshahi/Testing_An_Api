from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drfapp.serializers import StudentSerializer
from drfapp.models import Student


class TesView(APIView):
    permission_classes=[IsAuthenticated,]
    def get(self,request, *args, **kwargs):
        qs=Student.objects.all()
        first=qs.first()
        serializer=StudentSerializer(first)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()   
           return Response(serializer.data)
        return Response(serializer.errors)
        