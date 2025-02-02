from django.urls import path, include

urlpatterns = [
    ...
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from faqs import views

router = DefaultRouter()
router.register(r'faqs', views.FAQViewSet)

urlpatterns = [
    ...
    path('api/', include(router.urls)),
]