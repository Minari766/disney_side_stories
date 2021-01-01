from django.views.generic import View
from django.shortcuts import render,redirect
from .models import Post
from .models import Post, Area, Attraction, Category
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.formtools.preview import FormPreview


class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by("-id")
        return render(request, 'app/index.html', {
            'post_data': post_data,
        })

class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_detail.html', {
            'post_data': post_data
        })

class CreatePostView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        return render(request, 'app/post_form.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post()
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            area = form.cleaned_data['area']
            post_data.area = Area.objects.get(name=area)
            attraction = form.cleaned_data['attraction']
            post_data.attraction = Attraction.objects.get(name=attraction)
            category = form.cleaned_data['category']
            post_data.category = Category.objects.get(name=category)
            post_data.content = form.cleaned_data['content']
            if request.FILES:
                post_data.image = request.FILES.get('image')
            # .save()で入力データをDBに保存
            # post_data.save()
            # return redirect('post_detail', post_data.id)
            return render(request, 'app/post_preview.html', {
                'post_data' : post_data
            })

# 以下コードはformｂのvalidationが失敗したとき
        return render(request, 'app/post_form.html', {
            'form': form
        })

class PreviewPostView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        print('test4')
        post_data = Post()
        area = request.POST.get('area')
        post_data.area = Area.objects.get(name=area)
        attraction = request.POST.get('attraction')
        post_data.attraction = Attraction.objects.get(name=attraction)
        category = request.POST.get('category')
        post_data.category = Category.objects.get(name=category)
        post_data.save()
        print('test5')
        return redirect('index')

class PostEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostForm(
            request.POST or None,
            initial={
                'title': post_data.title,
                'area': post_data.area,
                'attraction': post_data.attraction,
                'category': post_data.category,
                'content': post_data.content,
                'image': post_data.image,
            }
        )

        return render(request, 'app/post_form.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.title = form.cleaned_data['title']
            area = form.cleaned_data['area']
            area_data = Area.objects.get(name=area)
            post_data.area = area_data
            attraction = form.cleaned_data['attraction']
            attraction_data = Attraction.objects.get(name=attraction)
            post_data.attraction = attraction_data
            category = form.cleaned_data['category']
            category_data = Attraction.objects.get(name=category)
            post_data.category = category_data
            post_data.content = form.cleaned_data['content']
            if request.FILES:
                post_data.image = request.FILES.get('image')
            post_data.save()
            return redirect('post_detail', self.kwargs['pk'])

        return render(request, 'app/post_form.html', {
            'form': form
        })

class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_delete.html', {
            'post_data': post_data
        })

    def post(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('index')


class AreaView(View):
    def get(self, request, *args, **kwargs):
        area_data = Area.objects.get(name=self.kwargs['area'])
        post_data = Post.objects.order_by('-id').filter(area=area_data)
        return render(request, 'app/index.html', {
            'post_data': post_data
        })

class AttractionView(View):
    def get(self, request, *args, **kwargs):
        attraction_data = Attraction.objects.get(name=self.kwargs['attraction'])
        post_data = Post.objects.order_by('-id').filter(attraction=attraction_data)
        return render(request, 'app/index.html', {
            'post_data': post_data
        })

class CategoryView(View):
    def get(self, request, *args, **kwargs):
        category_data = Category.objects.get(name=self.kwargs['category'])
        post_data = Post.objects.order_by('-id').filter(category=category_data)
        return render(request, 'app/index.html', {
            'post_data': post_data
        })

class BazaarView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by("-id")
        return render(request, 'app/bazaar.html', {
            'post_data': post_data,
        })

class FantasyView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by("-id")
        return render(request, 'app/fantasy.html', {
            'post_data': post_data,
        })

class CritterView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by("-id")
        return render(request, 'app/critter.html', {
            'post_data': post_data,
        })

class AdventureView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by("-id")
        return render(request, 'app/adventure.html', {
            'post_data': post_data,
        })

class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/about.html')

class MypageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/mypage.html')