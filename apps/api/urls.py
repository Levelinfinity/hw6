from django.urls import path

from .views import HelloApiView, Profile, ProjectInfoApiView

urlpatterns = [
    path('hello/', HelloApiView.as_view(), name='api-hello'),
    path('profile/', Profile.as_view(), name='api-profile'),
    path('about/', ProjectInfoApiView.as_view(), name='api-about'),
]

