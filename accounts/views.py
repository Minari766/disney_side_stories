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
        like_count = like_data.count()
        print("like_count", like_count)
        mypost_data = Post.objects.order_by('-id').filter(author=request.user) 
        post_count = mypost_data.count()
        print("post_count", post_count)
        page_obj_like = self.paginate_queryset(request, like_data, 5)
        print(page_obj_like)
        # print(page_obj_like.object_list)
        page_obj_mypost = self.paginate_queryset(request, mypost_data, 5)
        print(page_obj_mypost)
        # print(page_obj_mypost.object_list)

        like_all = 0
        for post in mypost_data:
            count = post.like_set.count()
            like_all += count
        print("like_all", like_all)
        return render(request, 'accounts/profile.html', {
            'user_data': user_data,
            'like_data': page_obj_like.object_list,
            'mypost_data': page_obj_mypost.object_list,
            'page_obj_like': page_obj_like,
            'page_obj_mypost': page_obj_mypost,
            'post_count': post_count,
            'like_all': like_all
        })

class MyPostViewTwo(LoginRequiredMixin, View):
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
        like_count = like_data.count()
        print("like_count", like_count)
        mypost_data = Post.objects.order_by('-id').filter(author=request.user) 
        mypost_count = mypost_data.count()
        print("mypost_count", mypost_count)
        post_count = mypost_data.count()
        page_obj_like = self.paginate_queryset(request, like_data, 5)
        page_obj_mypost = self.paginate_queryset(request, mypost_data, 5)

        like_all = 0
        for post in mypost_data:
            count = post.like_set.count()
            like_all += count
        print("like_all", like_all)
        return render(request, 'accounts/mypost.html', {
            'user_data': user_data,
            'like_data': page_obj_like.object_list,
            'mypost_data': page_obj_mypost.object_list,
            'page_obj_like': page_obj_like,
            'page_obj_mypost': page_obj_mypost,
            'post_count': post_count,
            'like_all': like_all
        })

class ProfileEditView(LoginRequiredMixin, View):
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
            # ここからコピー
            like_data = Like.objects.order_by('-id').filter(author=request.user)
            like_count = like_data.count()
            print("like_count", like_count)
            # like_all = Like.objects.all().count()
            # print("like_all", like_all)
            mypost_data = Post.objects.order_by('-id').filter(author=request.user) 
            post_count = mypost_data.count()
            print("post_count", post_count)
            page_obj_like = self.paginate_queryset(request, like_data, 5)
            page_obj_mypost = self.paginate_queryset(request, mypost_data, 5)

            like_all = 0
            for post in mypost_data:
                count = post.like_set.count()
                like_all += count
            print("like_all", like_all)
            # ここまで
            user_data.user_name = form.cleaned_data['user_name']
            if request.FILES:
                user_data.icon = request.FILES.get('icon')
            user_data.save()
            return render(request, 'accounts/profile.html', {
            'user_data': user_data,
            # ここから
            'like_data': page_obj_like.object_list,
            'mypost_data': page_obj_mypost.object_list,
            'page_obj_like': page_obj_like,
            'page_obj_mypost': page_obj_mypost,
            'post_count': post_count,
            'like_all': like_all
            # ここまで
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

class MainProfView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        like_data = Like.objects.order_by('-id').filter(author=request.user)
        like_count = like_data.count()
        print("like_count", like_count)
        mypost_data = Post.objects.order_by('-id').filter(author=request.user) 
        post_count = mypost_data.count()
        print("post_count", post_count)

        like_all = 0
        for post in mypost_data:
            count = post.like_set.count()
            like_all += count
        print("like_all", like_all)
        return render(request, 'accounts/mainprof.html', {
            'user_data': user_data,
            'post_count': post_count,
            'like_all': like_all
        })