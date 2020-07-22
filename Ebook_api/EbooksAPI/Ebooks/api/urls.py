#from django.conf.urls import url
from django.urls import path
#from rest_framework_swagger.views import get_swagger_view

from Ebooks.api.views import (EbookDetailAPIView, EbooksListCreateAPIView, 
                              ReviewCreateAPIView, ReviewDetailAPIView)                          

#schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path("ebooks/", EbooksListCreateAPIView.as_view(),name="ebook_list" ),
    path("ebooks/<int:pk>/", EbookDetailAPIView.as_view(),name="ebook_detail" ),
    #url(r'^$', schema_view)
    path("ebooks/<int:ebook_pk>/review",ReviewCreateAPIView.as_view(),name="ebook_review"),
    path("reviews/<int:pk>/",ReviewDetailAPIView.as_view(),name="review_detail"),
]
  