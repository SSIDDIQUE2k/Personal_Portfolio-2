Backend: Django API (Railway-ready)

Overview
- Django 5 + DRF + CORS + Whitenoise
- PostgreSQL via `DATABASE_URL` (fallback to SQLite locally)
- Ready for Railway deploy using `gunicorn`

Local Setup
- Create a virtualenv and install deps:
  - python -m venv .venv && source .venv/bin/activate
  - pip install -r requirements.txt
- Copy env and run migrations:
  - cp .env.example .env
  - python backend/manage.py migrate
- Run dev server:
  - python backend/manage.py runserver 8000

Key Env Vars
- SECRET_KEY: Django secret key
- DEBUG: "1" for local dev, empty for prod
- ALLOWED_HOSTS: comma list (e.g. "+.railway.app,localhost")
- DATABASE_URL: e.g. postgres://... from Railway
- CORS_ALLOWED_ORIGINS: comma list of allowed origins
- CSRF_TRUSTED_ORIGINS: comma list, include Railway URL and Angular host

Deploy on Railway
- Create a Python service from this repo
- Set env vars above (Railway will inject PORT)
- Migrations command (deploy hook): `python backend/manage.py migrate`
- Start command (Procfile): `gunicorn config.wsgi --chdir backend --preload --bind 0.0.0.0:$PORT`

API
- Health: GET `/api/health/` → {"status":"ok"}
- Projects: GET `/api/projects/`, GET `/api/projects/:id/`
- Skills: GET `/api/skills/`, GET `/api/skills/:id/`
- Experiences: GET `/api/experiences/`, GET `/api/experiences/:id/`
- Contact: POST `/api/contact/` → {id, name, email, subject, body, created_at}

Notes
- Data endpoints are read-only by default (no auth yet).
- Contact accepts JSON body: {name, email, subject?, body}.

Next Steps
- Share Angular API needs (routes, payloads) and we’ll align serializers/views.
# Personal_Portfolio-2
