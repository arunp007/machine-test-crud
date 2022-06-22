from django.urls import path
from.import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('admin',views.admin, name='admin'),
    path('registration', views.registration, name = 'registration'),
    path('regtable',views.regtable, name = 'regtable'),
    path('update<int:id>', views.update, name = 'update'),
    path('delete<int:id>', views.delete, name = 'delete'),
    path('student_register', views.student_register, name='student'),
    path('student_login', views.student_login, name='student'),
    path('logout_admin',views.logout_admin, name='logout_admin'),
    path('logout_student',views.logout_student, name='logout_student')
]