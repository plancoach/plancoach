from django.urls import path

from profile_introductionapp.views import Profile_introductionCreateView, Profile_introductionUpdateView, \
    Profile_introductionDeleteView

app_name = 'profile_introductionapp'

urlpatterns = [
    path('create/<int:pk>', Profile_introductionCreateView.as_view(), name='create'),
    path('update/<int:pk>',Profile_introductionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>',Profile_introductionDeleteView.as_view(), name='delete'),
]