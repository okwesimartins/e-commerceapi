from django.urls import path
from .views import article_list
from .views import article_detail
from .views import RegisterView, LoginView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from .views import register
urlpatterns = [
    path('article/',article_list),
    path('register/',RegisterView.as_view()),
    # path('login/',LoginView.as_view()),
    
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register/',register),
    path('detail/<int:pk>/',article_detail),
]