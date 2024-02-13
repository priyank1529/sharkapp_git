from django.views.generic import TemplateView
from django.urls import path
from . import views
from chatapp.views.auth_views import CustomLoginView
from chatapp.views.simple_view import SharkCreateView,SharkUpdateView
urlpatterns=[
    path('login1',CustomLoginView.as_view(),name="login"),
    path('add_shark',SharkCreateView.as_view(),name="add_shark"),
    path('<int:pk>/update_shark',SharkUpdateView.as_view(),name="update_shark")
    
]