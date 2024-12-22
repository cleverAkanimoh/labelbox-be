from rest_framework.viewsets import ModelViewSet
from .models import AnnotationProject, Task, Annotation
from .serializers import AnnotationProjectSerializer, TaskSerializer, AnnotationSerializer


class AnnotationProjectViewSet(ModelViewSet):
    queryset = AnnotationProject.objects.all()
    serializer_class = AnnotationProjectSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class AnnotationViewSet(ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
