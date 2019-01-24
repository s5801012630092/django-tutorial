from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('input/',views.input, name='input'),
    # path('output/',views.output, name='output')
]