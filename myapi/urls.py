
from django.contrib import admin
from django.urls import path
from myapi import views
from .views import african_countries
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('students/', views.student_list),
    path('', african_countries, name='country_list'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
