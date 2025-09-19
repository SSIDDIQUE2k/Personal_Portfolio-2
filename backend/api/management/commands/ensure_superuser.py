import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create or update a Django superuser from environment variables if none exists."

    def handle(self, *args, **options):
        User = get_user_model()

        # Support both Django's conventional env names and simpler aliases
        username = (
            os.environ.get("DJANGO_SUPERUSER_USERNAME")
            or os.environ.get("SUPERUSER_USERNAME")
        )
        email = (
            os.environ.get("DJANGO_SUPERUSER_EMAIL")
            or os.environ.get("SUPERUSER_EMAIL")
            or "admin@example.com"
        )
        password = (
            os.environ.get("DJANGO_SUPERUSER_PASSWORD")
            or os.environ.get("SUPERUSER_PASSWORD")
        )

        if not username or not password:
            self.stdout.write(
                self.style.WARNING(
                    "ensure_superuser: Skipping — SUPERUSER env vars not set (DJANGO_SUPERUSER_USERNAME/PASSWORD)."
                )
            )
            return

        try:
            user, created = User.objects.get_or_create(username=username, defaults={"email": email})
            user.is_staff = True
            user.is_superuser = True
            if password:
                user.set_password(password)
            if email and user.email != email:
                user.email = email
            user.save()
            if created:
                self.stdout.write(self.style.SUCCESS(f"ensure_superuser: Created superuser '{username}'."))
            else:
                self.stdout.write(self.style.SUCCESS(f"ensure_superuser: Updated superuser '{username}'."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"ensure_superuser: Failed — {e}"))

