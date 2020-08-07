
from django.urls import path, include
#from .views import article_list, article_detail
from .views import ArticleAPIView, ArticleDetails
from .views import GenericAPIView
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet,
                basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),

    #path('article/', article_list), #api view
    path('article/', ArticleAPIView.as_view()), #class based api views 
    #path('detail/<int:pk>/', article_detail), #api view
    path('detail/<int:id>/', ArticleDetails.as_view()), #class based api views
    path('generic/article/<int:id>/', GenericAPIView.as_view()), #generic class based api view
]