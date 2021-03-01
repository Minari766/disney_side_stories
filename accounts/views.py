from django.views import View
from accounts.models import CustomUser
from accounts.forms import ProfileForm, SignupUserForm
from django.shortcuts import render, redirect
from allauth.account import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

# Create your views here.
class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)

        return render(request, 'accounts/profile.html', {
            'user_data': user_data,
        })

class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        form = ProfileForm(
            request.POST or None,
            initial={
                'user_name': user_data.user_name,
                'icon': user_data.icon,
            }
        )
        return render(request, 'accounts/profile_edit.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user_data = CustomUser.objects.get(id=request.user.id)
            user_data.user_name = form.cleaned_data['user_name']
            if request.FILES:
                user_data.icon = request.FILES.get('icon')
            user_data.save()
            return render(request, 'accounts/profile.html', {
            'user_data': user_data,
        })
        # このreturnはis_valid()（バリデーション機能）に問題があった場合にprofile画面にリダイレクトするようにする
        return render(request, 'accounts/profile.html', {
            'form': form
        })

class LoginView(views.LoginView):
    template_name = 'accounts/login.html'


class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')


class SignupView(views.SignupView):
    template_name = 'accounts/signup.html'
    form_class = SignupUserForm
    
    # form_valid(self, form)
