from rest_framework import serializers
from Ebooks.models import Ebooks, Review

class ReviewSerializer(serializers.ModelSerializer):

    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = "__all__" 
    
class EbooksSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True,read_only = True)

    class Meta:
        model = Ebooks
        fields = "__all__"