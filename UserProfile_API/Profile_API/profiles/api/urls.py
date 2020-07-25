from django.urls import path, include
from .views import ProfileViewSet, ProfileStatusViewSet, AvatarUpadateView
from rest_framework.routers import DefaultRouter

# using the router we can create diffent endpoint very easily.
router = DefaultRouter()
router.register(r"profiles", ProfileViewSet) 
router.register(r"status", ProfileStatusViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("avatar/", AvatarUpadateView.as_view(), name = "avatar_update")
]




# profile_list = ProfileViewSet.as_view({"get" : "list"})
# profile_detail = ProfileViewSet.as_view({"get" : "retrieve"})

# urlpatterns = [
#     path("profiles/", profile_list, name="profile-lIst"),
#     path("profiles/<int:pk>", profile_detail, name="profile-detail")
#]