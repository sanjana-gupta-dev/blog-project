from django.contrib import admin
from django.urls import path
from blog.views import blog_home, about, add_post, delete_post, edit_post
from django.contrib.auth import views as auth_views
from blog.views import signup

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog_home),
    path('about/', about),
    path('add/', add_post),
    path('delete/<int:index>/', delete_post),
    path('edit/<int:index>/', edit_post),  
    path('signup/', signup),

    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)