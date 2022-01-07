from django.urls import path
from .views import HomePageView, SnackListView, SnackDetailView

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('snacks-list/', SnackListView.as_view(), name='snacks-view'),
        path('snacks-detail/', SnackDetailView.as_view(), name='snacks-detail')
]