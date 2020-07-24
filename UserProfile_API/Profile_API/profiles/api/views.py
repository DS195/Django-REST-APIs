from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile, ProfileStatus
from .serializers import (ProfileSerializer, 
                         ProfileAvatarSerializer,
                         ProfileStatusSerializers)

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

