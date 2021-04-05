from django.urls import path
from .views import ResourcesApi, TotalView

urlpatterns = [
    path('resources',  ResourcesApi.as_view()),
    path('total_cost', TotalView.as_view()),
]
