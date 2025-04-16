"""
URL configuration for flight_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view to handle the root path
def home(request):
    return HttpResponse("Welcome to the Flight Booking App!")

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('api/accounts/', include('accounts.urls')),  # Assuming you have an accounts app
    path('', home),  # Root path that returns the welcome message
    path('api/auth/', include('dj_rest_auth.urls')),  # dj_rest_auth for authentication (login, logout)
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Registration route for user signup
]
