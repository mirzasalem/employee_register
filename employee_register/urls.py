
from django.urls import path, include
from .import views

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),
    path('<int:id>/', views.employee_form,name='employee_update'),
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/', views.employee_list, name='employee_list'),
    path('login/', views.employee_login, name='employee_login'),
    path('register/', views.employee_register, name='employee_register'),
    path('log_out/', views.log_out, name='log_out'),#employee.profile_image.url
    path('profile_image/', views.employee_profile_image, name='employee_profile_image'),
    # path('employee/', include('employee_register.urls')),

    # path('list/', views.empl)
] 