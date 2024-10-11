from django.urls import path
from snippets import views

urlpatterns = [
    path('', views.snippet_list),  # This matches /snippets/
    path('<int:pk>/', views.snippet_detail),  # This matches /snippets/<id>/
]

