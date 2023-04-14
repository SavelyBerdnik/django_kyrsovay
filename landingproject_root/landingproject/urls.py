"""landingproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from crm import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets

from crm.views import OrdersAPIView, CommentCrmAPIView, OrdersViewSet
from price.views import PriceTableAPIView, PriceCardAPIView, PriceTableViewSet

router = routers.SimpleRouter()
router.register('prices', PriceTableViewSet, basename='price')
router.register('orders', OrdersViewSet, basename='order')
# router.register(r'comment', CommentCrmAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/v1/priceTableList/', PriceTableAPIView.as_view()),
    path('api/v1/priceCardList/', PriceCardAPIView.as_view()),
    path('api/', include(router.urls)),
    path('thanks/', views.thanks_page, name='thanks_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
