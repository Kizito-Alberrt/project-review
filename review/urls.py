from django.urls import path
from django.urls import path
# from . import views
from .views import Home,review
    
urlpatterns = [ 
    # path('', views.home, name='home'),
    path('', Home.as_view(), name='home'),
    path('review/<int:pk>', review.as_view(), name='review'),
]

    
