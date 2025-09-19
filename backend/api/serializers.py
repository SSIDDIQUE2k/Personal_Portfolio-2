from rest_framework import serializers
from .models import Profile, Project, Skill, Experience, Education, Message, Footer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'url', 'repo_url', 'image_url',
            'tags', 'order', 'featured', 'created_at', 'updated_at'
        ]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            'id', 'name', 'level', 'category', 'order', 'created_at', 'updated_at'
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'id', 'company', 'role', 'start_date', 'end_date', 'summary',
            'highlights', 'order', 'created_at', 'updated_at'
        ]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'id', 'institution', 'degree', 'field_of_study', 'start_date', 
            'end_date', 'description', 'location', 'order', 'created_at', 'updated_at'
        ]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'name', 'email', 'subject', 'body', 'created_at']
        read_only_fields = ['created_at']


class FooterLinkSerializer(serializers.Serializer):
    label = serializers.CharField()
    href = serializers.CharField()


class FooterSerializer(serializers.ModelSerializer):
    links = FooterLinkSerializer(many=True, required=False)

    class Meta:
        model = Footer
        fields = ['enabled', 'title', 'subtitle', 'links', 'show_socials', 'copyright_text', 'updated_at']
