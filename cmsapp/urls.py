from django.urls import path
from cmsapp import views

urlpatterns=[

    path('base',views.base),
    path('',views.login),
    path('home',views.home),
    path('header',views.header),
    path('footer',views.footer),
    path('login',views.login),
    path('signup',views.signup),
    path('product',views.product),
    path('logout', views.logout, name='logout'),

]