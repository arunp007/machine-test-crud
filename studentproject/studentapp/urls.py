from django.urls import path
from.import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logintable', views.logintable, name='logintable'),
    path('admin',views.admin, name='admin'),
    path('registration', views.registration, name = 'registration'),
    path('regtable',views.regtable, name = 'regtable'),
    path('update<int:id>', views.update, name = 'update')
]