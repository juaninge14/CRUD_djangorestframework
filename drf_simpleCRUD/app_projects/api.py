from app_projects.models import Project
from rest_framework import viewsets, permissions

from app_projects.serializer import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer