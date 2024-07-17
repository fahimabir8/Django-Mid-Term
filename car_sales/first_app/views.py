from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,update_session_auth_hash,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from . import forms
from car.models import Car 
from django.urls import reverse_lazy 
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('homepage')
        
    else:
        form = forms.RegistrationForm()
    
    return render(request, 'register.html', {'form': form })



class UserLoginView(LoginView):
    template_name = 'register.html'
    form_class = AuthenticationForm
    
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
      
def user_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'profile.html')

def update_profile(request):
    if request.method == "POST":
        form = forms.UserUpdateForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Update Successfully")
            
        else:
            messages.warning(request, "Profile Update Failed !!")
            return redirect('profile')
        
    else:
        form = forms.UserUpdateForm(instance = request.user)
    
    return render(request, 'update_profile.html', {'form': form})
    
