from django.urls import include, path
from .import views
from .import api




urlpatterns = [
    path('home',views.home,name='home'),
    path('register',views.new_register,name='new_register'),
    path('login',views.new_login,name='new_login'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contact',views.contact,name='contact'),
    path('header',views.header,name='header'),
    path('footer',views.footer,name='footer'),
    path('navbar',views.navbar,name='navbar'),
    path('api/list',api.registerapi,name='registerapi'),
     path('api/list/<int:id>/',api.lgoicl,name='lgoicl'),
    
]
