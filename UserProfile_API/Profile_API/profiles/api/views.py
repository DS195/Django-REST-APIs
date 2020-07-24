from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile, ProfileStatus
from .serializers import (ProfileSerializer, 
                         ProfileAvatarSerializer,
                         ProfileStatusSerializers)
from rest_framework.viewsets import ReadOnlyModelViewSet


class ProfileViewSet(ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

