from rest_framework import serializers
from .models import AnnotationProject, Task, Annotation

class AnnotationProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnotationProject
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = '__all__'
