
from django.urls import path ,include
from . import views
from django.conf.urls.static import static
urlpatterns = [

    path('',views.index,name='home'),
    path('index',views.index,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('archive', views.archive_view.as_view(), name='blog_archive'),
    path('<slug:slug>', views.blog_detail, name='blog_detail'),]
