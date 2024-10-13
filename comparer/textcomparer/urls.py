from django.urls import path
from .views import compare_texts, test_view, test_view_post

urlpatterns = [
    path('test/', test_view, name='compare_texts'),
    path('test_post/', test_view_post, name='compare_texts'),
    path('compare/', compare_texts, name='compare_texts'),
]