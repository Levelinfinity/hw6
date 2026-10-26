from django.urls import path

from .views import RegisterView, LoginView, LogOutView, ProfileView, TokenView, TokenLogOutView, JWTTokenLogOutView,JWTTokenView



urlpatterns = [
    path('login/token/', TokenView.as_view(), name='token'),
    path('logout/token/', TokenLogOutView.as_view(), name='token-out'),

    path('login/jwt/', JWTTokenView.as_view(), name='token'),
    path('logout/jwt/refresh/', JWTTokenLogOutView.as_view(), name='token-out'),
    

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
