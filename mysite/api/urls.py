from django.urls import path, include
from . import viewsets, views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reviews', viewsets.ReviewPostViewset, basename='reviews')



urlpatterns = [
    path("blogpost/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blogpost/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name = "update"),
    path('', include(router.urls)),
]