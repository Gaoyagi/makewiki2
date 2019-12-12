from django.shortcuts import render

#import these things to use createview an usercreationform
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    #template_name is an inbuilt variable that will automatically tell django to render to this template
    #
    template_name = 'registration/signup.html'