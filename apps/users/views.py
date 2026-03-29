from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, CustomUserCreationForm, ProfileForm, User, UserUpdateForm

from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def register(request):
    # if request includes Post it's bound form, for validation if Post is empty (={}) it's None, an unbound form that don't need validation
    form = CustomUserCreationForm(request.POST or None) # don't need else in if request.POST block

    if request.method == "POST" and form.is_valid(): 
            form.save()
            
            next_url = request.GET.get('next') or '/'
            return redirect(next_url)
    
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    form = CustomAuthenticationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        username_or_email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username_or_email,password=password)
        if user is not None:
                login(request, user) # sets user sesion, which makes request.user accesable in whole app

                next_url = request.GET.get('next') or '/'  # after login return to prevois page
                return redirect(next_url)
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
        logout(request)
        next_url = request.GET.get('next') or '/'  # return to prevois page or home
        return redirect(next_url)
        
# User profile public view
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    context = {
        'profile_user': profile_user,
    }
    return render(request, 'users/profile.html', context)

# User profile edit view
@login_required
def profile_edit(request):

    profile = request.user.profile
    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    user_form = UserUpdateForm(request.POST or None, instance=request.user)
    password_form = PasswordChangeForm(request.user, request.POST or None)

    if request.method == "POST":
        if 'save_profile' in request.POST and profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('users:profile', username=request.user.username)
        
        if 'change_password' in request.POST and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in after password change
            return redirect('users:profile', username=request.user.username)

    context = {
        'profile_form': profile_form,
        'user_form': user_form,
        'password_form': password_form,
        'profile': profile,
    }

    return render(request, 'users/profile_edit.html', context)

