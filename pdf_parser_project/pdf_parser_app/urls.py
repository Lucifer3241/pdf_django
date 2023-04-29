from django.urls import path
from .views import MyDataListCreate, MyDataRetrieveUpdateDestroy

urlpatterns = [
    path('data/', MyDataListCreate.as_view(),name='restdata'),
    path('data/<int:pk>/', MyDataRetrieveUpdateDestroy.as_view()),
]