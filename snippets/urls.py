from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),  # This matches /snippets/
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),  # This matches /snippets/<id>/
    path('users/', views.UserList.as_view()), # User list view
    path('users/<int:pk>/', views.UserDetail.as_view()), # User detail view
]
urlpatterns = format_suffix_patterns(urlpatterns)
