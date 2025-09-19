from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_profile_image_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default Theme', max_length=100)),
                ('primary', models.CharField(default='#8b5cf6', help_text='Hex color, e.g. #8b5cf6', max_length=7)),
                ('secondary', models.CharField(default='#a855f7', max_length=7)),
                ('tertiary', models.CharField(default='#7c3aed', max_length=7)),
                ('accent', models.CharField(default='#c4b5fd', max_length=7)),
                ('title_color', models.CharField(default='#f8fafc', max_length=7)),
                ('text_color', models.CharField(default='rgba(248, 250, 252, 0.85)', max_length=32)),
                ('body_color', models.CharField(default='#0f0a1a', max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={'verbose_name': 'Theme', 'verbose_name_plural': 'Theme'},
        ),
    ]

