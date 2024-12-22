from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import AnnotationProjectViewSet, TaskViewSet, AnnotationViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('projects', AnnotationProjectViewSet)
router.register('tasks', TaskViewSet)
router.register('annotations', AnnotationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
