from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),  # This matches /snippets/
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),  # This matches /snippets/<id>/
]
urlpatterns = format_suffix_patterns(urlpatterns)
