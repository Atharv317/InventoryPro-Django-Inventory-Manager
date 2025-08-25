from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.http import JsonResponse
from inventory import views

def health(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('health/', health),
]
