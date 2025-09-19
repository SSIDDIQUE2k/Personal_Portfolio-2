from django.db import migrations


def create_default_theme(apps, schema_editor):
    Theme = apps.get_model('api', 'Theme')
    if not Theme.objects.exists():
        Theme.objects.create(
            id=1,
            name='Default Theme',
            primary='#8b5cf6',
            secondary='#a855f7',
            tertiary='#7c3aed',
            accent='#c4b5fd',
            title_color='#f8fafc',
            text_color='rgba(248, 250, 252, 0.85)',
            body_color='#0f0a1a',
        )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_theme'),
    ]

    operations = [
        migrations.RunPython(create_default_theme, noop),
    ]

