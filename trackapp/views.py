
from django.shortcuts import render, get_object_or_404, HttpResponse


#import SignUp modele here
from trackapp.models import SignUp


from trackapp.forms import SignUpForm
from trackapp.forms import LoginForm
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

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



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

#this method render /trackapp/home.html page

def signup(request):
    signupData=SignUpForm(request.POST)
    context={
        "signupData":signupData
    }
    print("sdkfksdfknfksfksfnsknfkjs")
    if request.method == 'POST':
        if signupData.is_valid():
            instance = signupData.save(commit=False)
            instance.save()
        print(signupData)
        return render(request,'trackapp/signup.html')
    else:
        print("page re gggggggggggg")
        return render(request,'trackapp/signup.html',context)

def login(request):
    loginData=LoginForm(request.POST)
    print("jai hind")
    context = {
        "loginData": loginData,
    }
    if request.method == 'POST':
        useremail = request.POST.get('useremail', '')
        password = request.POST.get('password', '')
        print("useremail: ",useremail)
        login_data = SignUp.objects.get(useremail=useremail)
        if login_data.password == password:
            request.session['signup_id'] = login_data.id
            print("session_id",request.session['signup_id'])
            return render(request,'trackapp/index.html',{})
        else:
            return render(request, 'trackapp/login.html', context)

    return render(request, 'trackapp/login.html', context)


def logout(request):
    try:
        del request.session['signup_id']
        print("request.session['signup_id']",request.session['signup_id'])
    except KeyError:
        pass
    print("request.session['signup_id']")
    return HttpResponse("You're logged out.")

def home(request):
    return render(request,'trackapp/home.html', {})