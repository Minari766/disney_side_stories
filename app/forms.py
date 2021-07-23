from django import forms
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import BadHeaderError, message, send_mail
from django.http import HttpResponse
from .models import Area, Attraction, Category


class PostForm(forms.Form):
    area_data = Area.objects.all()
    area_choice = {}
    for area in area_data:
        area_choice[area] = area
    
    attraction_data = Attraction.objects.all()
    attraction_choice = {}
    for attraction in attraction_data:
        attraction_choice[attraction] = attraction

    category_data = Category.objects.all()
    category_choice = {}
    for category in category_data:
        category_choice[category] = category
    
    title = forms.CharField(max_length=50, label='タイトル')
    area = forms.ChoiceField(label='エリア', widget=forms.Select, choices=list(area_choice.items()))
    attraction = forms.ChoiceField(label='アトラクション', widget=forms.Select, choices=list(attraction_choice.items()))
    category = forms.ChoiceField(label='カテゴリ', widget=forms.Select, choices=list(category_choice.items()))
    content = forms.CharField(label='内容', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像', required=False)

    def clean_area(self):
        area = self.cleaned_data.get('area')
        if area in ('選択'):
            self.add_error('area', 'エリアを選択してください')
        return area

CATEGORIES = (
    ('0', 'このサイトについて'),
    ('1', '投稿記事について'),
    ('2', '不具合について'),
    ('3', 'ご意見・ご要望'),
)
class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='Email', max_length=100)
    # cntct_category = forms.ChoiceField(label='カテゴリー', choices=CATEGORIES)
    message = forms.CharField(
        label='お問い合わせ内容',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "お問い合わせ内容",
        }),
    )
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name in ('ばか', 'あほ', 'まぬけ', 'うんこ', '死ね'):
            self.add_error('name', 'お名前に禁止ワードが含まれています')
        return name

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message in ('ばか', 'あほ', 'まぬけ', 'うんこ', '死ね'):
            self.add_error('message', 'お問い合わせ内容にに禁止ワードが含まれています')
        return message


# class ContactForm(forms.Form):
#     name = forms.CharField(
#         label='お名前',
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': "お名前",
#         }),
#     )
#     cntct_category = forms.ChoiceField(
#         label='カテゴリー',
#         choices=CATEGORIES
#     )
#     email = forms.EmailField(
#         label='',
#         widget=forms.EmailInput(attrs={
#             'class': 'form-control',
#             'placeholder': "メールアドレス",
#         }),
#     )
#     message = forms.CharField(
#         label='',
#         widget=forms.Textarea(attrs={
#             'class': 'form-control',
#             'placeholder': "お問い合わせ内容",
#         }),
#     )

#     def clean_name(self):
#         name = self.cleaned_data.get('name')
#         if name in ('ばか', 'あほ', 'まぬけ', 'うんこ', '死ね'):
#             self.add_error('name', 'お名前に禁止ワードが含まれています')
#         return name

#     def clean_message(self):
#         message = self.cleaned_data.get('message')
#         if message in ('ばか', 'あほ', 'まぬけ', 'うんこ', '死ね'):
#             self.add_error('name', 'お問い合わせ内容にに禁止ワードが含まれています')
#         return message

#     def send_email(self):
#         subject = "お問い合わせ"
#         message = self.cleaned_data['message']
#         cntct_category = self.cleaned_data['cntct_category']
#         name = self.cleaned_data['name']
#         email = self.cleaned_data['email']
#         from_email = '{name} <{email}>'.format(name=name, email=email)
#         recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
#         # recipient_list = ['kkeeper.ch@gmail.com']  # 受信者リスト
#         try:
#             send_mail(subject, cntct_category, message, from_email, recipient_list)
#         except BadHeaderError:
#             return HttpResponse("無効なヘッダが検出されました。")
#         return redirect('thanks')
    
#     def thanks(request):
#         return HttpResponse('Thank you for your message.')
