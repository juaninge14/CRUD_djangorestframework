from rest_framework import serializers
#from .models import Project         # que tambien se puede escribir como
from app_projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'Title', 'Description', 'Technology', 'Created_at')
        read_only_fields = ('Created_at',)               # Solo para leer

