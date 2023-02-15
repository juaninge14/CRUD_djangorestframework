from django.urls import path, include
    
from rest_framework import routers
from app_projects.api import ProjectViewSet


router = routers.DefaultRouter()
router.register('api/app_projects', ProjectViewSet, 'projects')
urlpatterns = router.urls