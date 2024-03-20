from django.urls import path
from .views import (
    PhoneNumberListCreateView,
    PhoneNumberDetailView,
    RegisterUserView,
    UserProfileView,
    UserContactsView,
    SearchPersonView,
    LoginView,
    UserView,
    LogoutView
)

urlpatterns = [
    path('numbers/', PhoneNumberListCreateView.as_view(), name='number-list'),
    path('numbers/<int:pk>/', PhoneNumberDetailView.as_view(), name='number-detail'),
    path('register/', RegisterUserView.as_view(), name='register-user'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('user/',UserView.as_view(),name='user'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('contacts/', UserContactsView.as_view(), name='user-contacts'),
    path('search/', SearchPersonView.as_view(), name='search-person'),
]
