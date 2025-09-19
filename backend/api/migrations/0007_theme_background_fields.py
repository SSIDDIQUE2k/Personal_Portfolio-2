from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_create_default_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='background_animation',
            field=models.CharField(choices=[('starfield', 'Starfield'), ('matrix', 'Matrix Rain'), ('none', 'None')], default='starfield', max_length=20),
        ),
        migrations.AddField(
            model_name='theme',
            name='overlay_scanlines',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='theme',
            name='show_hud',
            field=models.BooleanField(default=False, help_text='Show system status HUD overlay'),
        ),
        migrations.AddField(
            model_name='theme',
            name='show_progress',
            field=models.BooleanField(default=False, help_text='Show scanning progress bar overlay'),
        ),
    ]

