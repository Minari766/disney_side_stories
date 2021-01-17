from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render,redirect, get_object_or_404
from .models import Post, Area, Attraction, Category, Like
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
        area = self.kwargs.get('area')
        category = self.kwargs.get('category')
        print(category)
        # print("test")
        if area == 'bazaar':
            area_data = Area.objects.get(name='ワールドバザール')
            post_data = post_data.filter(area=area_data)
            if category == 'story':
                category_data = Category.objects.get(name='ストーリー')
                post_data = post_data.filter(category=category_data)
            elif category == 'mickey':
                category_data = Category.objects.get(name='隠れミッキー')
                post_data = post_data.filter(category=category_data)
            elif category == 'trivia':
                category_data = Category.objects.get(name='豆知識')
                post_data = post_data.filter(category=category_data)
            elif category == 'other':
                category_data = Category.objects.get(name='その他')
                post_data = post_data.filter(category=category_data)
            elif category == 'all':
                category_data = Category.objects.get(name='全て')
                post_data = post_data.filter(category=category_data)
        elif area == 'adventure':
            area_data = Area.objects.get(name='アドベンチャーランド')
            post_data = post_data.filter(area=area_data)
            if category == 'story':
                category_data = Category.objects.get(name='ストーリー')
                post_data = post_data.filter(category=category_data)
            elif category == 'mickey':
                category_data = Category.objects.get(name='隠れミッキー')
                post_data = post_data.filter(category=category_data)
            elif category == 'trivia':
                category_data = Category.objects.get(name='豆知識')
                post_data = post_data.filter(category=category_data)
            elif category == 'other':
                category_data = Category.objects.get(name='その他')
                post_data = post_data.filter(category=category_data)
            elif category == 'all':
                category_data = Category.objects.get(name='全て')
                post_data = post_data.filter(category=category_data)
        elif area == 'western':
            area_data = Area.objects.get(name='ウエスタンランド')
            post_data = post_data.filter(area=area_data)
            if category == 'story':
                category_data = Category.objects.get(name='ストーリー')
                post_data = post_data.filter(category=category_data)
            elif category == 'mickey':
                category_data = Category.objects.get(name='隠れミッキー')
                post_data = post_data.filter(category=category_data)
            elif category == 'trivia':
                category_data = Category.objects.get(name='豆知識')
                post_data = post_data.filter(category=category_data)
            elif category == 'other':
                category_data = Category.objects.get(name='その他')
                post_data = post_data.filter(category=category_data)
            elif category == 'all':
                category_data = Category.objects.get(name='全て')
                post_data = post_data.filter(category=category_data)
        elif area == 'critter':
            area_data = Area.objects.get(name='クリッターカントリー')
            post_data = post_data.filter(area=area_data)
            if category == 'story':
                category_data = Category.objects.get(name='ストーリー')
                post_data = post_data.filter(category=category_data)
            elif category == 'mickey':
                category_data = Category.objects.get(name='隠れミッキー')
                post_data = post_data.filter(category=category_data)
            elif category == 'trivia':
                category_data = Category.objects.get(name='豆知識')
                post_data = post_data.filter(category=category_data)
            elif category == 'other':
                category_data = Category.objects.get(name='その他')
                post_data = post_data.filter(category=category_data)
            elif category == 'all':
                category_data = Category.objects.get(name='全て')
                post_data = post_data.filter(category=category_data)
        elif area == 'fantasy':
            area_data = Area.objects.get(name='ファンタジーランド')
            post_data = post_data.filter(area=area_data)
            if category == 'story':
                category_data = Category.objects.get(name='ストーリー')
                post_data = post_data.filter(category=category_data)
            elif category == 'mickey':
                category_data = Category.objects.get(name='隠れミッキー')
                post_data = post_data.filter(category=category_data)
            elif category == 'trivia':
                category_data = Category.objects.get(name='豆知識')
                post_data = post_data.filter(category=category_data)
            elif category == 'other':
                category_data = Category.objects.get(name='その他')
                post_data = post_data.filter(category=category_data)
            elif category == 'all':
                category_data = Category.objects.get(name='全て')
                post_data = post_data.filter(category=category_data)
        elif area == 'toon':
            area_data = Area.objects.get(name='トゥーンタウン')
            post_data = post_data.filter(area=area_data)
            if category == 'story':
                category_data = Category.objects.get(name='ストーリー')
                post_data = post_data.filter(category=category_data)
            elif category == 'mickey':
                category_data = Category.objects.get(name='隠れミッキー')
                post_data = post_data.filter(category=category_data)
            elif category == 'trivia':
                category_data = Category.objects.get(name='豆知識')
                post_data = post_data.filter(category=category_data)
            elif category == 'other':
                category_data = Category.objects.get(name='その他')
                post_data = post_data.filter(category=category_data)
            elif category == 'all':
                category_data = Category.objects.get(name='全て')
                post_data = post_data.filter(category=category_data)
        elif area == 'tomorrow':
            area_data = Area.objects.get(name='トゥモローランド')
            post_data = post_data.filter(area=area_data)
            if category == 'story':
                category_data = Category.objects.get(name='ストーリー')
                post_data = post_data.filter(category=category_data)
            elif category == 'mickey':
                category_data = Category.objects.get(name='隠れミッキー')
                post_data = post_data.filter(category=category_data)
            elif category == 'trivia':
                category_data = Category.objects.get(name='豆知識')
                post_data = post_data.filter(category=category_data)
            elif category == 'other':
                category_data = Category.objects.get(name='その他')
                post_data = post_data.filter(category=category_data)
            elif category == 'all':
                category_data = Category.objects.get(name='全て')
                post_data = post_data.filter(category=category_data)
        elif area == 'all':
            if category == 'story':
                category_data = Category.objects.get(name='ストーリー')
                post_data = post_data.filter(category=category_data)
            elif category == 'mickey':
                category_data = Category.objects.get(name='隠れミッキー')
                post_data = post_data.filter(category=category_data)
            elif category == 'trivia':
                category_data = Category.objects.get(name='豆知識')
                post_data = post_data.filter(category=category_data)
            elif category == 'other':
                category_data = Category.objects.get(name='その他')
                post_data = post_data.filter(category=category_data)
            elif category == 'all':
                category_data = Category.objects.get(name='全て')
                post_data = post_data.filter(category=category_data)

        page_obj = self.paginate_queryset(request, post_data, 10)

        return render(request, 'app/index.html', {
            'post_data': page_obj.object_list,
            'page_obj': page_obj,
            'area': area,
            'category': category
        })


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        liked_list = []

        liked = post_data.like_set.filter(author=request.user)
        if liked.exists():
            liked_list.append(post_data.id)

        return render(request, 'app/post_detail.html', {
            'post_data': post_data,
            'liked_list': liked_list,
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
        category = self.kwargs.get('category')
        post_data = Category.objects.get(name=self.kwargs['category'])
        return render(request, 'app/index.html', {
            'post_data': post_data
        })

class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/about.html')

class MypageView(View):
    def get(self, request, *args, **kwargs):
        post_data = Like.objects.order_by('-id')
        return render(request, 'app/mypage.html', {
            'post_data': post_data
        })

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

def LikeView(request):
    if request.method =="POST":
        post = get_object_or_404(Post, pk=request.POST.get("post_id"))
        user = request.user
        liked = False
        like = Like.objects.filter(post=post, author=user)
        if like.exists():
            like.delete()
        else:
            like.create(post=post, author=user)
            liked = True
        
        context={
            'post_id': post.id,
            'liked': liked,
            'count': post.like_set.count(),
        }

        if request.is_ajax():
            return JsonResponse(context)

