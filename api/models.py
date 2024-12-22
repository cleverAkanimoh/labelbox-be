from django.db import models


class AnnotationProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Task(models.Model):
    project = models.ForeignKey(AnnotationProject, related_name='tasks', on_delete=models.CASCADE)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class Annotation(models.Model):
    task = models.ForeignKey(Task, related_name='annotations', on_delete=models.CASCADE)
    annotation_data = models.JSONField()  # Store annotation details as JSON
    created_at = models.DateTimeField(auto_now_add=True)
