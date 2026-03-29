from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    path('registration/', views.register, name='register'),
    #path('activate/<uidb64>/<token>/', views.activate, name='activate'), # Work in progress
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)