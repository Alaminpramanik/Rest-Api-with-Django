from django.urls import path
from posts.views import posts, post_details, PostAPIView , GenericAPIView

urlpatterns = [
    path('posts/', posts),
    path('details/', post_details),
    path('postapiview/', PostAPIView.as_view()), 
    path('generic/post/<int:id>/', GenericAPIView.as_view()), 

]
