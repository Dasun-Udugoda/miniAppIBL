from rest_framework import viewsets
from .models import ReviewPost
from .serializers import ReviewPostSerializers

class ReviewPostViewset(viewsets.ModelViewSet):
    queryset = ReviewPost.objects.all()
    serializer_class = ReviewPostSerializers
