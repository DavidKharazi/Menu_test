from django import template
from django.urls import resolve, reverse

from ..models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name, request):
    menu_items = MenuItem.objects.filter(parent__isnull=True, title=menu_name).prefetch_related('children')
    current_path = request.path
    current_url_name = resolve(current_path).url_name

    def render_menu_items(items):
        result = '<ul>'
        for item in items:
            ancestors = item.get_ancestors()
            is_active = item.url == current_path or item.url == reverse(current_url_name)
            if any(ancestor.url == current_path or ancestor.url == reverse(current_url_name) for ancestor in ancestors):
                is_active = True
            result += f'<li{" class=active" if is_active else ""}><a href="{item.url}">{item.title}</a>'
            if item.children.exists():
                result += render_menu_items(item.children.all())
            result += '</li>'
        result += '</ul>'
        return result

    return render_menu_items(menu_items)



