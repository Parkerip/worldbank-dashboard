from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Auth endpoint (login, returns token)
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),

    # ✅ Dashboard app routes
    path('api/', include('dashboard.urls')),
]
