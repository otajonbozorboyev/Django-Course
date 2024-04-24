from django.urls import path
from .views import indexView, blogView

urlpatterns = [
    path('', indexView, name='index'),
    path('blog/', blogView, name='blog'),
]