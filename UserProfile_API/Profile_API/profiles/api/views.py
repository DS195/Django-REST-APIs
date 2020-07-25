from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework import viewsets
from rest_framework import mixins

from profiles.models import Profile, ProfileStatus

from .serializers import (ProfileAvatarSerializer, ProfileSerializer,
                          ProfileStatusSerializers)
from profiles.api.permissions import IsOwnProfileOrReadOnly, IsOwnerOrReadOnly


'''
this class is using hight abstraction level and useful same as mixinclass
class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]
'''
class AvatarUpadateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        print(profile_object)
        return profile_object

class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]


class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializers
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)
