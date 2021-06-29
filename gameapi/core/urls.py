from django.urls import path

from .views import HelloView, get_tokens
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('',HelloView.as_view(), name='hello-view'),
    path('api/token/', get_tokens, name='token-pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]