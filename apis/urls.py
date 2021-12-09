from django.urls import path

from .views import ListFault , DetailFault

urlpatterns = [
    path('', ListFault.as_view()),
    path('<int:pk>/', DetailFault.as_view())
]