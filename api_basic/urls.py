
from django.urls import path
#from .views import article_list, article_detail
from .views import ArticleAPIView, ArticleDetails
from .views import GenericAPIView
urlpatterns = [
    #path('article/', article_list), #api view
    path('article/', ArticleAPIView.as_view()), #class based api views 
    #path('detail/<int:pk>/', article_detail), #api view
    path('detail/<int:id>/', ArticleDetails.as_view()), #class based api views
    path('generic/article/<int:id>/', GenericAPIView.as_view()), #generic class based api view
]