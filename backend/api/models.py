from django.db import models


class Profile(models.Model):
    """Single instance model for personal portfolio information"""
    # Personal Info
    name = models.CharField(max_length=100, default="Your Name")
    title = models.CharField(max_length=100, default="Frontend Developer")
    bio = models.TextField(default="I have high level experience in web design, development knowledge and producing quality work")
    
    # Images (either upload a file or provide a URL)
    home_image_file = models.ImageField(upload_to='profiles/', blank=True, null=True)
    about_image_file = models.ImageField(upload_to='profiles/', blank=True, null=True)
    home_image = models.URLField(blank=True, default="https://i.postimg.cc/3NgvPcZD/home-img.png")
    about_image = models.URLField(blank=True, default="https://i.postimg.cc/W1YZxTpJ/about-img.jpg")
    
    # About Section
    about_heading = models.CharField(max_length=200, default="Hi, I'm Your Name, based in Your Location")
    about_description = models.TextField(default="I'm a web developer, with extensive knowledge and years of experience, working with quality work in web technologies, UI and UX design")
    years_experience = models.CharField(max_length=20, default="10 +")
    projects_completed = models.CharField(max_length=20, default="60 +")
    support_availability = models.CharField(max_length=20, default="Online 24/7")
    
    # Contact Info
    email = models.EmailField(default="user@gmail.com")
    phone = models.CharField(max_length=20, default="999-888-777")
    messenger = models.CharField(max_length=50, default="user.fb123")
    
    # Social Links
    facebook_url = models.URLField(blank=True, default="https://www.facebook.com")
    instagram_url = models.URLField(blank=True, default="https://www.instagram.com")
    twitter_url = models.URLField(blank=True, default="https://www.x.com")
    
    # Resume/CV
    resume_url = models.URLField(blank=True, help_text="Link to your resume/CV")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
    
    def save(self, *args, **kwargs):
        # Ensure only one profile instance exists
        if not self.pk and Profile.objects.exists():
            raise ValueError("Only one Profile instance is allowed")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Profile - {self.name}"
    
    @classmethod
    def get_profile(cls):
        """Get the single profile instance, create if doesn't exist"""
        profile, created = cls.objects.get_or_create(pk=1)
        return profile


class Theme(models.Model):
    """Singleton model to control site color theme variables.

    These fields map to CSS variables consumed by the frontend styles.
    """
    name = models.CharField(max_length=100, default="Default Theme")
    primary = models.CharField(max_length=7, default="#8b5cf6", help_text="Hex color, e.g. #8b5cf6")
    secondary = models.CharField(max_length=7, default="#a855f7")
    tertiary = models.CharField(max_length=7, default="#7c3aed")
    accent = models.CharField(max_length=7, default="#c4b5fd")
    title_color = models.CharField(max_length=7, default="#f8fafc")
    text_color = models.CharField(max_length=32, default="rgba(248, 250, 252, 0.85)")
    body_color = models.CharField(max_length=7, default="#0f0a1a")

    BACKGROUND_CHOICES = (
        ("starfield", "Starfield"),
        ("matrix", "Matrix Rain"),
        ("cybergrid", "Cyber Grid"),
        ("particles", "Floating Particles"),
        ("scanlines", "Scanlines"),
        ("aurora", "Aurora Gradient"),
        ("waves", "Waves"),
        ("dots", "Dots"),
        ("none", "None"),
    )
    background_animation = models.CharField(max_length=20, choices=BACKGROUND_CHOICES, default="starfield")
    overlay_scanlines = models.BooleanField(default=False)
    show_hud = models.BooleanField(default=False, help_text="Show system status HUD overlay")
    show_progress = models.BooleanField(default=False, help_text="Show scanning progress bar overlay")
    
    SCOPE_CHOICES = (
        ("all", "All Sections"),
        ("home_only", "Home Section Only"),
    )
    background_scope = models.CharField(max_length=20, choices=SCOPE_CHOICES, default="all")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Theme"

    def save(self, *args, **kwargs):
        # Ensure only one Theme instance exists
        if not self.pk and Theme.objects.exists():
            raise ValueError("Only one Theme instance is allowed")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Theme - {self.name}"

    @classmethod
    def get_theme(cls):
        """Get the single theme instance, create with defaults if missing."""
        theme, _ = cls.objects.get_or_create(pk=1)
        return theme


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
    tags = models.JSONField(default=list, blank=True)
    order = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title


class Skill(TimeStampedModel):
    CATEGORY_CHOICES = (
        ("language", "Language"),
        ("framework", "Framework"),
        ("tool", "Tool"),
        ("other", "Other"),
    )
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=0)  # 0-100
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="other")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Education(TimeStampedModel):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-start_date"]

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Experience(TimeStampedModel):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    summary = models.TextField(blank=True)
    highlights = models.JSONField(default=list, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-start_date"]

    def __str__(self):
        return f"{self.role} @ {self.company}"


class Message(TimeStampedModel):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"


class Footer(models.Model):
    """Single instance model for footer content/settings."""
    enabled = models.BooleanField(default=True)
    title = models.CharField(max_length=200, blank=True, default="")
    subtitle = models.CharField(max_length=200, blank=True, default="")
    links = models.JSONField(default=list, blank=True, help_text="List of {label, href} objects")
    show_socials = models.BooleanField(default=True)
    copyright_text = models.CharField(max_length=300, blank=True, default="© Your Name. All rights reserved")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footer"

    def save(self, *args, **kwargs):
        if not self.pk and Footer.objects.exists():
            raise ValueError("Only one Footer instance is allowed")
        super().save(*args, **kwargs)

    def __str__(self):
        return "Footer Settings"

    @classmethod
    def get_footer(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
