from django.contrib import admin
from django.contrib.admin import AdminSite
from django.shortcuts import render
from django.urls import path
from django.db import models
from .models import Profile, Project, Skill, Education, Experience, Message, Theme, Footer

# Import the dashboard customization
from . import admin_dashboard
from .admin_dashboard import invalidate_dashboard_cache

# Customize the admin site
admin.site.site_header = "Portfolio Admin Dashboard"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'bio')
        }),
        ('Images', {
            'fields': ('home_image_file', 'about_image_file', 'home_image', 'about_image'),
            'description': 'Either upload images (preferred) or paste direct image URLs. Uploaded files will be used when present.'
        }),
        ('About Section', {
            'fields': ('about_heading', 'about_description', 'years_experience', 'projects_completed', 'support_availability')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'messenger')
        }),
        ('Social Links', {
            'fields': ('facebook_url', 'instagram_url', 'twitter_url')
        }),
        ('Resume', {
            'fields': ('resume_url',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one profile instance
        return not Profile.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion of the profile
        return False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "order", "created_at", "updated_at", "project_status")
    list_filter = ("featured", "created_at", "updated_at")
    search_fields = ("title", "description", "tags")
    ordering = ("order",)
    list_editable = ("featured", "order")
    list_per_page = 20
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'order', 'featured')
        }),
        ('Links & Media', {
            'fields': ('url', 'repo_url', 'image_url'),
            'description': 'Add project links and preview image'
        }),
        ('Tags & Metadata', {
            'fields': ('tags',),
            'description': 'Add relevant tags as a JSON array (e.g., ["React", "Node.js", "MongoDB"])'
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Auto-generate order if not set
        if not obj.order:
            max_order = Project.objects.aggregate(max_order=models.Max('order'))['max_order'] or 0
            obj.order = max_order + 1
            obj.save()
        # Invalidate cache
        invalidate_dashboard_cache()
    
    def project_status(self, obj):
        """Custom method to show project status"""
        if obj.featured:
            return "Featured"
        return "Regular"
    project_status.short_description = "Status"
    
    def make_featured(self, request, queryset):
        """Bulk action to make projects featured"""
        updated = queryset.update(featured=True)
        invalidate_dashboard_cache()
        self.message_user(request, f'{updated} projects marked as featured.')
    make_featured.short_description = "Mark selected projects as featured"
    
    def make_regular(self, request, queryset):
        """Bulk action to make projects regular"""
        updated = queryset.update(featured=False)
        invalidate_dashboard_cache()
        self.message_user(request, f'{updated} projects marked as regular.')
    make_regular.short_description = "Mark selected projects as regular"
    
    def duplicate_project(self, request, queryset):
        """Bulk action to duplicate projects"""
        for project in queryset:
            project.pk = None
            project.title = f"{project.title} (Copy)"
            project.order = Project.objects.aggregate(max_order=models.Max('order'))['max_order'] + 1
            project.save()
        invalidate_dashboard_cache()
        self.message_user(request, f'{queryset.count()} projects duplicated.')
    duplicate_project.short_description = "Duplicate selected projects"
    
    actions = [make_featured, make_regular, duplicate_project]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "level", "order", "created_at", "skill_level")
    list_filter = ("category", "level", "created_at")
    search_fields = ("name",)
    ordering = ("order",)
    list_editable = ("level", "order")
    list_per_page = 25
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'category', 'level', 'order')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request)
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Auto-generate order if not set
        if not obj.order:
            max_order = Skill.objects.aggregate(max_order=models.Max('order'))['max_order'] or 0
            obj.order = max_order + 1
            obj.save()
        # Invalidate cache
        invalidate_dashboard_cache()
    
    def skill_level(self, obj):
        """Custom method to show skill level with visual indicator"""
        if obj.level >= 80:
            return f"{obj.level}% (Expert)"
        elif obj.level >= 60:
            return f"{obj.level}% (Advanced)"
        elif obj.level >= 40:
            return f"{obj.level}% (Intermediate)"
        else:
            return f"{obj.level}% (Beginner)"
    skill_level.short_description = "Level"
    
    def set_expert_level(self, request, queryset):
        """Bulk action to set skills to expert level"""
        updated = queryset.update(level=90)
        invalidate_dashboard_cache()
        self.message_user(request, f'{updated} skills set to expert level.')
    set_expert_level.short_description = "Set selected skills to expert level"
    
    def set_advanced_level(self, request, queryset):
        """Bulk action to set skills to advanced level"""
        updated = queryset.update(level=70)
        invalidate_dashboard_cache()
        self.message_user(request, f'{updated} skills set to advanced level.')
    set_advanced_level.short_description = "Set selected skills to advanced level"
    
    def set_intermediate_level(self, request, queryset):
        """Bulk action to set skills to intermediate level"""
        updated = queryset.update(level=50)
        invalidate_dashboard_cache()
        self.message_user(request, f'{updated} skills set to intermediate level.')
    set_intermediate_level.short_description = "Set selected skills to intermediate level"
    
    actions = [set_expert_level, set_advanced_level, set_intermediate_level]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("institution", "degree", "field_of_study", "start_date", "end_date", "order", "created_at")
    list_filter = ("start_date", "end_date", "created_at")
    ordering = ("order",)
    search_fields = ("institution", "degree", "field_of_study")
    list_editable = ("order",)
    list_per_page = 20
    
    fieldsets = (
        ('Institution Information', {
            'fields': ('institution', 'degree', 'field_of_study', 'location', 'order')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date'),
            'description': 'Leave end_date empty if currently studying'
        }),
        ('Details', {
            'fields': ('description',),
            'description': 'Add description of your education'
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request)
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Auto-generate order if not set
        if not obj.order:
            max_order = Education.objects.aggregate(max_order=models.Max('order'))['max_order'] or 0
            obj.order = max_order + 1
            obj.save()
        # Invalidate cache
        invalidate_dashboard_cache()


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("company", "role", "start_date", "end_date", "order", "created_at")
    list_filter = ("start_date", "end_date", "created_at")
    ordering = ("order",)
    search_fields = ("company", "role", "summary")
    list_editable = ("order",)
    list_per_page = 20
    
    fieldsets = (
        ('Company Information', {
            'fields': ('company', 'role', 'order')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date'),
            'description': 'Leave end_date empty if currently working here'
        }),
        ('Details', {
            'fields': ('summary', 'highlights'),
            'description': 'Add summary and key highlights as JSON array'
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request)
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Auto-generate order if not set
        if not obj.order:
            max_order = Experience.objects.aggregate(max_order=models.Max('order'))['max_order'] or 0
            obj.order = max_order + 1
            obj.save()
        # Invalidate cache
        invalidate_dashboard_cache()


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "read", "reply_status")
    list_filter = ("read", "created_at")
    search_fields = ("name", "email", "subject", "body")
    ordering = ("-created_at",)
    list_per_page = 25
    list_editable = ("read",)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email')
        }),
        ('Message Details', {
            'fields': ('subject', 'body', 'read')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request)
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Invalidate cache
        invalidate_dashboard_cache()
    
    def reply_status(self, obj):
        """Custom method to show reply status"""
        if obj.read:
            return "Read"
        return "Unread"
    reply_status.short_description = "Status"
    
    def mark_as_read(self, request, queryset):
        """Bulk action to mark messages as read"""
        updated = queryset.update(read=True)
        invalidate_dashboard_cache()
        self.message_user(request, f'{updated} messages marked as read.')
    mark_as_read.short_description = "Mark selected messages as read"
    
    def mark_as_unread(self, request, queryset):
        """Bulk action to mark messages as unread"""
        updated = queryset.update(read=False)
        invalidate_dashboard_cache()
        self.message_user(request, f'{updated} messages marked as unread.')
    mark_as_unread.short_description = "Mark selected messages as unread"
    
    actions = [mark_as_read, mark_as_unread]


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ("name", "primary", "secondary", "tertiary", "accent", "background_animation", "overlay_scanlines", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Theme Colors", {
            'fields': ("name", "primary", "secondary", "tertiary", "accent")
        }),
        ("Text & Background", {
            'fields': ("title_color", "text_color", "body_color"),
            'description': "Optional overrides for text/background colors"
        }),
        ("Background Animation", {
            'fields': ("background_animation", "background_scope", "overlay_scanlines", "show_hud", "show_progress"),
            'description': "Choose the background animation and overlays for the site"
        }),
        ("Timestamps", {
            'fields': ("created_at", "updated_at"),
        }),
    )

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        from django import forms
        color_fields = {"primary", "secondary", "tertiary", "accent", "title_color", "body_color"}
        if db_field.name in color_fields:
            kwargs["widget"] = forms.TextInput(attrs={"type": "color"})
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def has_add_permission(self, request):
        # Only allow one Theme instance
        return not Theme.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("enabled", "title", "subtitle", "updated_at")
    readonly_fields = ("updated_at",)
    fieldsets = (
        ("Footer Content", {
            'fields': ("enabled", "title", "subtitle", "copyright_text")
        }),
        ("Links", {
            'fields': ("links",),
            'description': 'Add items like [{"label": "Services", "href": "#services"}]'
        }),
        ("Options", {
            'fields': ("show_socials",),
        }),
    )

    def has_add_permission(self, request):
        return not Footer.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
