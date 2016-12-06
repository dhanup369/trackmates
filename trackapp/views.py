
from django.shortcuts import render, get_object_or_404


#import SignUp modele here
from trackapp.models import SignUp

#import serializers model here
from trackapp.serializers import SignUpSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

#import other module
from datetime import datetime,timedelta
from django.utils import timezone


#  class based views for SignUp model model--------------------------------------------

class SignUpList(APIView):

    """
    List all SignUp or created a new SignUp

    """
    def get(self, request, format=None):
        signup = SignUp.objects.all()
        serializer  = SignUpSerializer(signup,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignUpDetail(APIView):
    """
    Retrive , update, or delete a SignUp instance.

    """
    def get_object(self,pk):
        try:
            return SignUp.objects.get(pk=pk)
        except SignUp.DoseNotExit:
            raise Http404
    def get(self, request, pk, format=None):
        signup = self.get_object(pk)
        serializer=SignUpSerializer(signup)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        signup=self.get_object(pk)
        serializer=SignUpSerializer(signup,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.status.HTTP_400_BAD_REQUESt)
    def delete(self, request, pk, format=None):
        signup=self.get_object(pk)
        signup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #print "datetime",timezone.now()

#----------------------end --------------------------------------------------------------


# this function for home page
def home(request):
    return render(request,'trackapp/home.html',{})
