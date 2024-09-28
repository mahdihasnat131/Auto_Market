from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from orders.models import Order
from django.views.generic import FormView
from .forms import Registrationform,ChangeUserForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class Register(FormView):
    template_name='register.html'
    form_class= Registrationform
    success_url=reverse_lazy('profile')

    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.success(self.request,'Information given is incorrect')
        return super().form_invalid(form)
    
class User_login(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    

# class User_logout(LogoutView):
#     def get_success_url(self):
#         if self.request.user.is_authenticated:
#             logout(self.request)
#         return reverse_lazy('home')

def User_logout(request):
    logout(request)
    return redirect('login')

    
@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'orders': orders})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})

