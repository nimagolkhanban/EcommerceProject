from django.urls import path
from userauths import views as userauths_view


urlpatterns = [
    path('user/token/', userauths_view.MyTokenObtainPairView.as_view()),
    path('user/register/', userauths_view.RegisterView.as_view()),
]