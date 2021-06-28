from django.urls import path

from .views import SearchView, ListCategoryView

urlpatterns = [
    path('api/search', SearchView.as_view(), name='search'),
    path('api/list', ListCategoryView.as_view(), name='list-view'),
]