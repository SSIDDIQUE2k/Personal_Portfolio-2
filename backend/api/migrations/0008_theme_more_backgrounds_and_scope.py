from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_theme_background_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='background_animation',
            field=models.CharField(choices=[('starfield', 'Starfield'), ('matrix', 'Matrix Rain'), ('cybergrid', 'Cyber Grid'), ('particles', 'Floating Particles'), ('scanlines', 'Scanlines'), ('aurora', 'Aurora Gradient'), ('waves', 'Waves'), ('dots', 'Dots'), ('none', 'None')], default='starfield', max_length=20),
        ),
        migrations.AddField(
            model_name='theme',
            name='background_scope',
            field=models.CharField(choices=[('all', 'All Sections'), ('home_only', 'Home Section Only')], default='all', max_length=20),
        ),
    ]

