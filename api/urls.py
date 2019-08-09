#urls.py pour définir où nous pouvons trouver des informations

from django.urls import path
from .views import SiteListApiView, VMListApiView, GatewayListApiView, TerminalListApiView, ServiceListApiView, SiteRetrieveApiView, VMRetrieveApiView, GatewayRetrieveApiView, TerminalRetrieveApiView, ServiceRetrieveApiView, UserListView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

app_name = 'api'

urlpatterns = [
    path('site/', SiteListApiView.as_view()),
    path('site/<int:pk>/', SiteRetrieveApiView.as_view()),
    path('vm/', VMListApiView.as_view()),
    path('vm/<int:pk>/', VMRetrieveApiView.as_view()),
    path('gateway/', GatewayListApiView.as_view()),
    path('gateway/<int:pk>/', GatewayRetrieveApiView.as_view()),
    path('terminal/', TerminalListApiView.as_view()),
    path('terminal/<int:pk>/', TerminalRetrieveApiView.as_view()),
    path('service/', ServiceListApiView.as_view()),
    path('service/<int:pk>/', ServiceRetrieveApiView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('token/obtain/',jwt_views.TokenObtainPairView.as_view(),name='token_obtain'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('userlist/', UserListView.as_view()),
]