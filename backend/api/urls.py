from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'skills', views.SkillViewSet, basename='skill')
router.register(r'experiences', views.ExperienceViewSet, basename='experience')
router.register(r'education', views.EducationViewSet, basename='education')
router.register(r'contact', views.MessageCreateViewSet, basename='contact')

urlpatterns = [
    path('health/', views.health, name='api-health'),
    path('profile/', views.profile_detail, name='profile'),
    path('footer/', views.footer_detail, name='footer'),
    path('', include(router.urls)),
]
