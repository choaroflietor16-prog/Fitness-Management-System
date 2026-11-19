# Fitness Management System · Kenfit

A Flask foundation for a personal-training portal. This milestone implements account registration, sign-in, sign-out and a protected dashboard. New self-registered accounts receive the client role.

## Application structure

| Path | Responsibility |
| --- | --- |
| `run.py` | WSGI entry point invoking the Flask application factory. |
| `config.py` and `.env.example` | Session key and database configuration, with SQLite for local development. |
| `app/__init__.py` | Application factory, Flask-SQLAlchemy, Flask-Login, Flask-Migrate and blueprint registration. |
| `app/auth/` | Registration and sign-in forms and routes. |
| `app/main/` | Public home and authenticated dashboard. |
| `app/models.py` | User model and Werkzeug password hashing. |
| `app/templates/` and `app/static/` | Jinja views and CSS. |

The user table stores an ID, first and last name, unique indexed email, password hash, role, creation timestamp and account status flag. The role helpers distinguish administrator, trainer and client. The current route flow is:

| Route | Purpose |
| --- | --- |
| `/` | Public landing page |
| `/auth/register` | Register a client account via GET/POST |
| `/auth/login` | Sign in via GET/POST |
| `/auth/logout` | Sign out of an authenticated session |
| `/dashboard` | View the logged-in user's dashboard |

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Create the local SQLite directory with `mkdir -p instance`. Set `SECRET_KEY` in `.env` to a fresh private value. The example uses `DATABASE_URL=sqlite:///kenfit.db`. For a fresh checkout, bootstrap migrations locally because the repository tree has no migration directory:

```bash
python -m flask --app run db init
python -m flask --app run db migrate -m "Create users"
python -m flask --app run db upgrade
python -m flask --app run
```

Open `http://127.0.0.1:5000/`. If a migration directory already exists, use the existing revisions and run `db upgrade`. Check registration, duplicate-email handling, invalid credentials, direct dashboard access while signed out and logout using synthetic accounts. If SQLite reports a missing user table, check the active database URL and migration status.

The application factory and blueprints provide a foundation for adding workflows independently. Next steps include tracking a verified baseline migration, building the booking and trainer availability calendar, and adding trainer dashboards, session credits and billing.
