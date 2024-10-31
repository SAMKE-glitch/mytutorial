from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('', views.api_root),  # API Root View
    path('snippets/', views.SnippetList.as_view()),  # Snippets list
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),  # Snippet detail
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),  # Snippet highlight view
    path('users/', views.UserList.as_view()),  # User list
    path('users/<int:pk>/', views.UserDetail.as_view()),  # User detail
]

urlpatterns = format_suffix_patterns(urlpatterns)

