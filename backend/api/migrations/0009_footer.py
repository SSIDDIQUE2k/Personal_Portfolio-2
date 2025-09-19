from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_theme_more_backgrounds_and_scope'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, default='', max_length=200)),
                ('subtitle', models.CharField(blank=True, default='', max_length=200)),
                ('links', models.JSONField(blank=True, default=list, help_text='List of {label, href} objects')),
                ('show_socials', models.BooleanField(default=True)),
                ('copyright_text', models.CharField(blank=True, default='© Your Name. All rights reserved', max_length=300)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={'verbose_name': 'Footer', 'verbose_name_plural': 'Footer'},
        ),
    ]

