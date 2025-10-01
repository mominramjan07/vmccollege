from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    

    # 🔹 Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='user_login'), name='user_logout'),

    # 🔹 Certificates app
    path('', include('certificates.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
