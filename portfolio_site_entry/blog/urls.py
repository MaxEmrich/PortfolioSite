from django.urls import path, include
from .views import Index
from .views import Index, DetailArticleView, LikeArticle, Featured

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'), # this is saying: when we go to the "" path on our webpage, go to the 'index' class in views and call that get index function  
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('featured/', Featured.as_view(), name='featured'), 
]         