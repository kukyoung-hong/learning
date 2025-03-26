from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles  # 모델 임포트
from django.core.paginator import Paginator  

def home(request):
    category_id = request.GET.get('category')
    page = request.GET.get('page', '1')  # 페이지
    if category_id:
        articles = Articles.objects.filter(category=category_id)
    else:
        articles = Articles.objects.all()
    paginator = Paginator(articles,10)
    page_obj = paginator.get_page(page)
    return render(request, 'myapp/home.html',{'articles':page_obj})


# Create your views here.
