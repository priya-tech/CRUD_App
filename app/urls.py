from django.urls import path
from .views import HomePageView, AddEntryView, UpdateEntryView, DeleteEntryView

urlpatterns = [
    path('home', HomePageView.as_view(), name='home_url'),
    path('add_entry', AddEntryView.as_view(), name='add_entry'),
    path('edit_entry/<str:pk>', UpdateEntryView.as_view(), name='edit_entry'),
    path('delete_entry/<str:pk>', DeleteEntryView.as_view(), name='delete_entry')
]