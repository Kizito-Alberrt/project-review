from django.urls import path
from django.urls import path


from .views import Home,review,AddPostView, update, delete,likeview
    
urlpatterns = [ 
    # path('', views.home, name='home'),
    path('', Home.as_view(), name='home'),
    path('review/<int:pk>', review.as_view(), name='review'),
    path('post/', AddPostView.as_view(), name='post'),
    path('article/edit/<int:pk>',update.as_view(), name='update'),
    path('article/<int:pk>/delete',delete.as_view(), name='delete'),
    path('like/<int:pk>', likeview, name='like'),
    
]

    
