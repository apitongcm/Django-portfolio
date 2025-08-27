from django.urls import path
from .views import PostViewSet, PostRetrieveUpdateDestroyView, Feedback


urlpatterns = [
    path('posts/', PostViewSet.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('feedback/',Feedback.as_view(), name='feedback-create'),
]
