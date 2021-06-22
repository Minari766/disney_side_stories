from django.views import View
from app.views import PostDetailView
from app.models import Post, Area, Attraction, Category, Like
from accounts.models import CustomUser
from accounts.forms import ProfileForm, SignupUserForm
from django.shortcuts import render, redirect
from allauth.account import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class ProfileView(LoginRequiredMixin, View):
    def paginate_queryset(self, request, queryset, count):
        paginator = Paginator(queryset, count)
        page = request.GET.get('page')
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        # page_obj:全体何ページ中のXページ目かを定義
        return page_obj

    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        like_data = Like.objects.order_by('-id').filter(author=request.user)
        mypost_data = Post.objects.order_by('-id').filter(author=request.user) 
        post_count = Post.objects.order_by('-id').filter(author=request.user).count()
        print(post_count) 
        # post_data = Post.objects.get(id=self.kwargs['pk'])
        # if request.user.is_authenticated:
        #     liked = post_data.like_set.filter(author=request.user)
        # else:
        #     liked = post_data.like_set.all()
    
        # if liked.exists():
        #     liked_list.append(post_data.id)
        page_obj_like = self.paginate_queryset(request, like_data, 3)
        page_obj_mypost = self.paginate_queryset(request, mypost_data, 5)

        return render(request, 'accounts/profile.html', {
            'user_data': user_data,
            'like_data': like_data,
            'mypost_data': mypost_data,
            'page_obj_like': page_obj_like,
            'page_obj_mypost': page_obj_mypost,
            'post_count': post_count,
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

