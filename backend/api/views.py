from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, mixins
import os

from .models import Profile, Project, Skill, Education, Experience, Message, Theme, Footer
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    SkillSerializer,
    ExperienceSerializer,
    EducationSerializer,
    MessageSerializer,
    FooterSerializer,
)


@api_view(["GET"])  # GET /api/health/
@permission_classes([AllowAny])
def health(request):
    return Response({
        "status": "ok",
        "env": "debug" if (os.environ.get('DEBUG', '') not in ('', '0', 'false', 'False')) else "prod",
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def profile_detail(request):
    """Get the single profile instance"""
    profile = Profile.get_profile()
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def footer_detail(request):
    footer = Footer.get_footer()
    serializer = FooterSerializer(footer)
    return Response(serializer.data)


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class MessageCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


def home_view(request):
    """Homepage view with profile data"""
    profile = Profile.get_profile()
    projects = Project.objects.filter(featured=True).order_by('order')[:6]  # Show featured projects first
    skills = Skill.objects.all().order_by('order')
    education = Education.objects.all().order_by('order')
    experiences = Experience.objects.all().order_by('order')
    
    context = {
        'profile': profile,
        'projects': projects,
        'skills': skills,
        'education': education,
        'experiences': experiences,
        'theme': Theme.get_theme(),
        'footer': Footer.get_footer(),
    }
    return render(request, 'index.html', context)
