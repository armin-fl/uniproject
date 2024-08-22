
from django.urls import path ,include
from . import views
from django.conf.urls.static import static
urlpatterns = [

    path('',views.blog_list,name='home'),

]
