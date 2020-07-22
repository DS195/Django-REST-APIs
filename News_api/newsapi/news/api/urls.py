from django.urls import path
from .views import (ArticleListCreateAPIView,
                   ArticleDetailAPIView,
                   JournalistListCreateAPIView) 
#from .views import (article_list_create_api_view,
#                  article_detail_api_view)


urlpatterns = [
    
    #path("articles/", article_list_create_api_view, name ="article-list"),
    #path("articles/<int:pk>", article_detail_api_view, name ="article-list-detail"),
    path("articles/", 
        ArticleListCreateAPIView.as_view(), 
        name ="article-list"),
    path("articles/<int:pk>", 
        ArticleDetailAPIView.as_view(), 
        name ="article-list-detail"),
    path("journalists/",
        JournalistListCreateAPIView.as_view() ,
        name ="journalist-list"),
    # path("journalists/<int:pk>",
    #     JournalistDetailAPIView.as_view(), 
    #     name ="journalist-list-detail"
    #     )
]