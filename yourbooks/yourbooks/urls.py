from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('accounts/', include('accounts.urls')),
]

# urlpatterns += static(setiing)