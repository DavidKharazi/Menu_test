
from django.contrib import admin
from django.urls import path, include  # Включаем функцию include() для добавления маршрутов из приложений

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu_app/', include('menu_app.urls')),  # Включаем маршруты из приложения

]
