from django.urls import path

from .views import SearchView, ListCategoryView

urlpatterns = [
    path('api/v1/search', SearchView.as_view(), name='search'),
    path('api/v1/list', ListCategoryView.as_view(), name='list-view'),
]