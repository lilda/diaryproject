"""diaryproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import diary.views
import account.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', diary.views.home, name="home"),
    path('delete/<int:diary_id>', diary.views.delete, name="delete"),
    path('update/<int:diary_id>', diary.views.update, name="update"),
    path('detail/<int:diary_id>', diary.views.detail, name="detail"),
    path('create/', diary.views.create, name="create"),
    path('like/<int:diary_id>', diary.views.like, name="like"),
    path('join', account.views.join, name="join"),
    path('login', account.views.login, name="login"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)