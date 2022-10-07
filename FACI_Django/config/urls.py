"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from Pages.homePage import views as homeViews
from Pages.EditPage import views as editViews
from Pages.GuidePage import views as guideViews
from Pages.ContactPage import views as contactViews
from Pages.logo_makingPage import views as logo_makingViews
from Pages.examplePage import views as examplePageViews
from Pages.ResultPage import views as resultPageViews



urlpatterns = [

    # path('주소', 뷰, 주소의 별명)
    path('admin/', admin.site.urls),
    path('guide/', guideViews.index, name="guide"),
    path('lock/', contactViews.lock, name="lock"),
    path('write/', contactViews.write, name="write"),
    path('message/', contactViews.message, name="message"),
    path('example/', examplePageViews.index, name="example"),
    path('logo_making/', logo_makingViews.index, name="logo_making"),
    #path('contact/', contactViews.index, name="contact"),
    path('color/', resultPageViews.color, name="color"),
    path('result/', resultPageViews.result, name="result"),
    path('edit/', editViews.index, name="edit"),
    path('loading/', resultPageViews.loading, name="loading"),
    path('home/', homeViews.index, name="home"),
    path('imgtool/', resultPageViews.imgtool, name="imgtool"),
    path('contact/', include('Board.urls')),
    path('', homeViews.index), #위에서 매칭된 뷰가 없을 경우 이쪽으로 연결되기 때문에 맨 아래에 위치하는것이 좋음
]

