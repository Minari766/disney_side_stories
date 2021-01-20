from django import forms
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
    area = forms.ChoiceField(label='カテゴリ', widget=forms.Select, choices=list(category_choice.items()))
    content = forms.CharField(label='内容', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像', required=False)
