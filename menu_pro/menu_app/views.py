
from .models import MenuItem
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'home.html')


def page_detail(request, slug):
    main_menu_items = MenuItem.objects.filter(parent=None).prefetch_related('children')
    page = get_object_or_404(MenuItem, slug=slug)
    return render(request, 'home.html',  {'main_menu_items': main_menu_items, 'page': page})