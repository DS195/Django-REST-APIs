from rest_framework import generics, mixins, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from Ebooks.api.pagination import SmallSetPagination
from Ebooks.api.permissions import (IsAdminUserOrReadOnly,
                                    IsReviewAuthorOrReadonly)
from Ebooks.api.serializer import EbooksSerializer, ReviewSerializer
from Ebooks.models import Ebooks, Review


class EbooksListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebooks.objects.all().order_by("-id")
    serializer_class = EbooksSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination
class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebooks.objects.all()
    serializer_class = EbooksSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        print(ebook_pk)
        ebook = get_object_or_404(Ebooks, pk=ebook_pk)
        print(ebook)
        review_author = self.request.user
        review_queryset = Review.objects.filter(ebook = ebook, review_author = review_author)
        if review_queryset.exists():
            return ValidationError("YOu have already reviewed the book")

        serializer.save(ebook=ebook, review_author=review_author)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadonly]



#class EbooksListCreateAPIView(mixins.ListModelMixin,
    #                         mixins.CreateModelMixin,
    #                         generics.GenericAPIView):

    # queryset = Ebooks.objects.all()
    # serializer_class = EbooksSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
