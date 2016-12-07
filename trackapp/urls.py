
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from trackapp import views

urlpatterns = [
    url(r'^signup_api/$', views.AdminSignUpList.as_view()),
    url(r'^signup_api/(?P<pk>[0-9]+)/$', views.SignUpDetail.as_view()),
    url(r'^signup_api/(?P<username>\w+)/$', views.SignUpDetail.as_view()),

    url(r'^si2chip/login/$', views.AdminLogin.as_view()),

    # urls for home.html(?P<username>\w+)
    url(r'^home/$', views.home, name='home'),

    # url for signup
    url(r'^signup/$', views.signup, name='signup'),

    # url for login
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

