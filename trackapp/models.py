from django.db import models

# Create your models here.
class SignUp(models.Model):
    username=     models.CharField( max_length=200, blank=False, null=True)
    useremail=    models.EmailField(max_length=250,blank=False, null=True)
    password=     models.CharField(max_length=250,blank=False, null=True)
    contact=      models.IntegerField(blank=True, null=True)
    designation=  models.CharField(max_length=250,blank=True, null=True)
    address=      models.TextField(blank=True, null=True)
    created_date= models.DateTimeField(auto_now_add=True)
    isAdmin=      models.BooleanField(default=False)
    isSupportEngineer=  models.BooleanField(default=False)
    isClient=      models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.useremail)


