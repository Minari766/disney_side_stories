from django import forms
from .models import Category, Attraction


class PostForm(forms.Form):
    category_data = Category.objects.all()
    category_choice = {}
    for category in category_data:
        category_choice[category] = category
    
    attraction_data = Attraction.objects.all()
    attraction_choice = {}
    for attraction in attraction_data:
        attraction_choice[attraction] = attraction

    title = forms.CharField(max_length=50, label='タイトル')
    category = forms.ChoiceField(label='カテゴリ', widget=forms.Select, choices=list(category_choice.items())) # 追加
    attraction = forms.ChoiceField(label='アトラクション', widget=forms.Select, choices=list(attraction_choice.items())) # 追加
    content = forms.CharField(label='内容', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像', required=False)