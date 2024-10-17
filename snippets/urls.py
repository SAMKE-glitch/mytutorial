from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('', views.snippet_list),  # This matches /snippets/
    path('<int:pk>/', views.snippet_detail),  # This matches /snippets/<id>/
]
urlpatterns = format_suffix_patterns(urlpatterns)
