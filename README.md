# Django Blog + Listings

A multi-app Django project that combines a blog, a listings/ads module ("ogloszenia"), and a custom user system with profile editing. It also integrates the `django_admin_ai` admin extension.

## Features
- Blog app with authors, categories, tags, and posts
- Listings/ads app with priced posts
- Custom user model with profile (avatar, bio, email visibility)
- Custom authentication backend and profile edit flow
- Admin AI integration (optional, configured via env)

## Tech Stack
- Python 3.x
- Django 6.x (see `manage.py` and `config/` settings)
- `django-environ` for environment variables
- `django_admin_ai` for admin enhancements

## Project Structure
- `apps/blog` - blog models, views, templates
- `apps/ogloszenia` - listings/ads app
- `apps/users` - custom user model, auth, profiles
- `config/settings` - base, dev, and prod settings
- `templates/` - shared templates

## Quickstart (Development)
1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

Note: `requirements.txt` is currently empty in this repo. At minimum you will need `Django`, `django-environ`, and `django_admin_ai`.

3. Create a local env file:

```bash
copy .env.example .env
```

4. Fill in required variables in `.env` (see `.env.example`).

5. Run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

The development settings are used by default via `manage.py` (`config.settings.dev`).

## Settings Overview
- `config/settings/base.py` - shared settings
- `config/settings/dev.py` - development overrides (DEBUG on, SQLite default)
- `config/settings/prod.py` - production overrides (security and email)

## Environment Variables
See `.env.example` for the full list. Common values:
- `SECRET_KEY` (required)
- `DEBUG` (true/false)
- `ALLOWED_HOSTS` (comma-separated)
- `DATABASE_URL` (optional in dev, required in prod)
- `OPENAI_API_KEY` and `OPENAI_MODEL` (for admin AI)
- `EMAIL_*` (required in prod if using SMTP)

## Useful URLs
- `http://127.0.0.1:8000/` - home
- `http://127.0.0.1:8000/blog/` - blog
- `http://127.0.0.1:8000/ogloszenia/` - listings
- `http://127.0.0.1:8000/users/` - users
- `http://127.0.0.1:8000/admin/` - Django admin
- `http://127.0.0.1:8000/admin-ai/` - admin AI (if enabled)

## Notes
- This project uses a custom user model: `users.User`.
- Media uploads are stored under `media/`.

