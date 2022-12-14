from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('registration', views.registration, name='registration'),
    path('continue_registration', views.continue_registration, name='continue_registration'),
    path('div_info', views.div_info, name='div_info'),
    path('divisions', views.divisions, name='divisions'),
    path('menu', views.menu, name='menu'),
    path('new_division', views.new_division, name='new_division'),
    path('students', views.students, name='students'),
    path('student_profile', views.student_profile, name='student_profile'),
    path('signin', views.signin, name='signin')
]
