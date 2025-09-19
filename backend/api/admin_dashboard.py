from django.contrib import admin
from django.template.response import TemplateResponse
from django.db.models import Count, Q
from django.utils import timezone
from django.core.cache import cache
from datetime import datetime, timedelta
from .models import Profile, Project, Skill, Education, Experience, Message

def admin_dashboard_view(request):
    """
    Enhanced admin dashboard view with comprehensive portfolio statistics
    """
    # Cache key for dashboard data
    cache_key = 'admin_dashboard_data'
    cached_data = cache.get(cache_key)
    
    if cached_data:
        return TemplateResponse(request, 'admin/index.html', cached_data)
    
    now = timezone.now()
    last_30_days = now - timedelta(days=30)
    last_7_days = now - timedelta(days=7)
    
    # Basic counts with caching
    project_count = cache.get('project_count')
    if project_count is None:
        project_count = Project.objects.count()
        cache.set('project_count', project_count, 300)  # 5 minutes
    
    skill_count = cache.get('skill_count')
    if skill_count is None:
        skill_count = Skill.objects.count()
        cache.set('skill_count', skill_count, 300)
    
    message_count = cache.get('message_count')
    if message_count is None:
        message_count = Message.objects.count()
        cache.set('message_count', message_count, 300)
    
    education_count = cache.get('education_count')
    if education_count is None:
        education_count = Education.objects.count()
        cache.set('education_count', education_count, 300)
    
    experience_count = cache.get('experience_count')
    if experience_count is None:
        experience_count = Experience.objects.count()
        cache.set('experience_count', experience_count, 300)
    
    # Recent activity counts
    recent_messages_count = Message.objects.filter(created_at__gte=last_7_days).count()
    recent_projects_count = Project.objects.filter(created_at__gte=last_7_days).count()
    unread_messages_count = Message.objects.filter(read=False).count()
    featured_projects_count = Project.objects.filter(featured=True).count()
    
    # Recent content
    recent_messages = Message.objects.order_by('-created_at')[:5]
    recent_projects = Project.objects.order_by('-created_at')[:5]
    recent_experiences = Experience.objects.order_by('-created_at')[:3]
    
    # Skills by category
    skills_by_category = Skill.objects.values('category').annotate(count=Count('id')).order_by('-count')
    
    # Monthly activity data for charts
    monthly_data = []
    for i in range(6):
        month_start = now - timedelta(days=30*i)
        month_end = month_start + timedelta(days=30)
        month_projects = Project.objects.filter(created_at__gte=month_start, created_at__lt=month_end).count()
        month_messages = Message.objects.filter(created_at__gte=month_start, created_at__lt=month_end).count()
        monthly_data.append({
            'month': month_start.strftime('%b'),
            'projects': month_projects,
            'messages': month_messages
        })
    
    # Top skills by level
    top_skills = Skill.objects.order_by('-level')[:5]
    
    # Recent activity timeline
    activity_timeline = []
    
    # Add recent messages to timeline
    for msg in recent_messages[:3]:
        activity_timeline.append({
            'type': 'message',
            'title': f'New message from {msg.name}',
            'description': msg.subject or msg.body[:50] + '...' if len(msg.body) > 50 else msg.body,
            'time': msg.created_at,
            'icon': 'fas fa-envelope',
            'color': 'primary'
        })
    
    # Add recent projects to timeline
    for project in recent_projects[:3]:
        activity_timeline.append({
            'type': 'project',
            'title': f'Project: {project.title}',
            'description': project.description[:50] + '...' if len(project.description) > 50 else project.description,
            'time': project.created_at,
            'icon': 'fas fa-project-diagram',
            'color': 'success'
        })
    
    # Sort timeline by time
    activity_timeline.sort(key=lambda x: x['time'], reverse=True)
    
    context = {
        'title': 'Portfolio Dashboard',
        # Basic counts
        'project_count': project_count,
        'skill_count': skill_count,
        'message_count': message_count,
        'education_count': education_count,
        'experience_count': experience_count,
        
        # Enhanced metrics
        'recent_messages_count': recent_messages_count,
        'recent_projects_count': recent_projects_count,
        'unread_messages_count': unread_messages_count,
        'featured_projects_count': featured_projects_count,
        
        # Recent content
        'recent_messages': recent_messages,
        'recent_projects': recent_projects,
        'recent_experiences': recent_experiences,
        
        # Analytics data
        'skills_by_category': skills_by_category,
        'monthly_data': monthly_data,
        'top_skills': top_skills,
        'activity_timeline': activity_timeline[:6],  # Show only 6 most recent activities
        
        # Chart data
        'chart_labels': [data['month'] for data in reversed(monthly_data)],
        'chart_projects': [data['projects'] for data in reversed(monthly_data)],
        'chart_messages': [data['messages'] for data in reversed(monthly_data)],
    }
    
    # Cache the context data for 5 minutes
    cache.set(cache_key, context, 300)
    
    return TemplateResponse(request, 'admin/index.html', context)

# Override the default admin index
def custom_admin_index(self, request, extra_context=None):
    """
    Custom admin index view
    """
    app_list = self.get_app_list(request)
    
    context = {
        **self.each_context(request),
        'title': self.index_title,
        'app_list': app_list,
        'project_count': Project.objects.count(),
        'skill_count': Skill.objects.count(),
        'message_count': Message.objects.count(),
        'experience_count': Experience.objects.count(),
        **(extra_context or {}),
    }
    
    return TemplateResponse(request, 'admin/index.html', context)

# Cache invalidation functions
def invalidate_dashboard_cache():
    """Invalidate dashboard cache when data changes"""
    cache.delete('admin_dashboard_data')
    cache.delete('project_count')
    cache.delete('skill_count')
    cache.delete('message_count')
    cache.delete('education_count')
    cache.delete('experience_count')

# Monkey patch the admin site
admin.site.index = custom_admin_index.__get__(admin.site, admin.AdminSite)
