"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from articles import views
from articles.views import get_article,create_post,login_fun,register_fun
from django.contrib.auth import views as authViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name='archive'),
    url(r'^article/(?P<article_id>\d+)$', get_article, name='get_article'),
    path('admin/articles/new/', create_post, name ='create_post'),
    path('register', register_fun, name ='register_fun'), 
    path('autho', login_fun, name ='login_fun'),
    path('exit', authViews.LogoutView.as_view(template_name="exit.html"), name ='exit'),
    
    
]
