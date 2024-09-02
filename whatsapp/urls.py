from django.urls import path
from .views import ActivitiesView

urlpatterns = [
    path('webhook',ActivitiesView.as_view(),name='webhook')
]
