from rest_framework import serializers
from trackapp.models import SignUp

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=SignUp
        fields = ('id','username','useremail','password','contact','designation','address','created_date','isAdmin','isSupportEngineer','isClient')