from django.contrib import admin
from django.urls import path
from .views import home, Create, Edit, search, MeetingDetailView, Update, MeetDeleteView

urlpatterns = [


    path('', home, name='index'),

    path('create/', Create.as_view(), name='add'),

    path('edit/', Edit.as_view(), name='edit'),

    path('search/', search, name='search'),

    path('meetingdetail/<int:pk>', MeetingDetailView.as_view(), name='meetingdetail'),

    path('update/<int:pk>', Update.as_view(), name='update'),

    path('delete/<int:pk>', MeetDeleteView.as_view(), name='delete'),

]
