from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('searchbooks/', views.searchbooks),
    path('bookdetails', views.bookdetails),
    # path('login', views.login),
    # path('signup', views.signup),
]

# urlpatterns += static(setiing)