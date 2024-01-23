from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from . models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


# Registration Class Based View
class CustomRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login') 
    
    
# Login Class Based View
class CustomLoginView(LoginView):
    template_name = 'account/login.html'  # Create a login.html template
    success_url = reverse_lazy('home')
    
# Logout Views    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')         

@method_decorator(login_required, name='dispatch')
class ProfileView(LoginRequiredMixin, View):
    template_name = 'account/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'user': request.user})
