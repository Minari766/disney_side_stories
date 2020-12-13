from .models import Category, Attraction

def common(request):
    category_data = Category.objects.all()
    attraction_data = Attraction.objects.all()
    context = {
        'category_data': category_data,
        'attraction_data': attraction_data,
    }
    return context
