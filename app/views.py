from django.views.generic import View
# from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import render,redirect
from .models import Post, Area, Attraction, Category
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
# or検索するために必要なQオブジェクトを取得
from django.db.models import Q
# 畳み込み演算を行う
from functools import reduce
# 足算に必要
from operator import and_
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class IndexView(View):
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
        post_data = Post.objects.order_by("-id")
        page_obj = self.paginate_queryset(request, post_data, 10)
        return render(request, 'app/index.html', {
            # object_list:クエリセットで使える変数
            'post_data': page_obj.object_list,
            'page_obj': page_obj, 
        })


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_detail.html', {
            'post_data': post_data
        })

class CreatePostView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # formには投稿記事の内容が、カテゴリの選択欄含めたくさんでている
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
        # POSTのPOST（データ入力フォームに記載された情報）の中身をリクエストして表示している。
        # print(request.POST)
        post_data = Post()
        area = request.POST.get('area')
        post_data.area = Area.objects.get(name=area)
        attraction = request.POST.get('attraction')
        post_data.attraction = Attraction.objects.get(name=attraction)
        category = request.POST.get('category')
        post_data.category = Category.objects.get(name=category)
        # request.userでログインユーザー情報を入手できる。
        post_data.author = request.user
        post_data.content = request.POST.get('content')
        post_data.image = request.POST.get('image')
        # if request.FILES:
        #         post_data.image = request.FILES.get('image')
        post_data.title = request.POST.get('title')
        post_data.save()
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
            category_data = Category.objects.get(name=category)
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
        # area_data = Area.objects.get(name="ファンタジーランド")
        # post_data = Post.objects.order_by("-id").filter(area=area_data)
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

class CategoryNameView(View):
    def get(self, request, *args, **kwargs):
        #self.kwargsでurlから値を取得する
        # path('category/<str:category>/'の<str:category>に動的に入る値を獲得する
        # inputボタンは押してないので、.getは不要
        category_data = Category.objects.get(name=self.kwargs['category'])
        post_data = Post.objects.filter(category=category_data)
        return render(request, 'app/index.html', {
            'post_data' : post_data
        })

class SearchView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by('-id')
        keyword = request.GET.get('keyword')

        if keyword:
            exclusion_list = set([' ', ' '])
            query_list = ''
            for word in keyword:
                if not word in exclusion_list:
                    # スペースを除いたリストを抽出
                    query_list += word
            # Qオブジェクトを使用して、投稿データをキーワードでフィルターがけする。キーワードをQオブジェクトでor検索
            query = reduce(and_, [Q(title__icontains=q) | Q(content__icontains=q) for q in query_list])
            post_data = post_data.filter(query)
        
        return render(request, 'app/search.html', {
            'keyword' : keyword,
            'post_data' : post_data
        })
