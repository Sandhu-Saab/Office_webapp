from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.router, name="router"),
    path('home/', views.home, name="home"),
    path('logout/', views.logout, name="logout"),
    path('login_page/', views.login_page, name="login_page"),
    path('add_trainer/', views.add_trainer, name="add_trainer"),
    path('edit_trainer/<int:trainer_id>', views.edit_trainer, name="edit_trainer"),
    path('lerning_path/', views.lerning_path, name="lerning_path"),
    path('add_lerning_path/', views.add_lerning_path, name="add_lerning_path"),
    path('trainer_info/<int:trainer_id>', views.trainer_info, name="trainer_info"),
    path('search_a_trainer/', views.search_a_trainer, name="search_a_trainer"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

