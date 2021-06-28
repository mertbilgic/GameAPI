from django.urls import path

from .views import HelloView, get_tokens

urlpatterns = [
    path('',HelloView.as_view(), name='hello-view'),
    path('api/token/', get_tokens, name='token-pair'),
]