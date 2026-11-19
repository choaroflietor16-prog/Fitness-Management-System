# Fitness Management System (Kenfit)

A booking, workout, meal-plan, and progress-tracking platform for personal trainers — built first for Kenfit at Virgin Active, designed to be rebranded for other trainers later.

## Milestone 1 — Done
- Project structure (app factory pattern, blueprints)
- Database setup (SQLAlchemy + Flask-Migrate)
- User model with roles (`admin`, `trainer`, `client`)
- Authentication: register, login, logout (Flask-Login + Flask-WTF)
- Landing page
- Placeholder dashboard (redirect target after login)

## Milestone 2 — Next
- Booking system (1-on-1, group, camps)
- Trainer availability calendar

## Setup

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create your .env file
cp .env.example .env
# then open .env and set a real SECRET_KEY

# 4. Create the instance folder (holds the SQLite db)
mkdir -p instance

# 5. Initialize the database
flask db init
flask db migrate -m "Initial migration - users table"
flask db upgrade

# 6. Run the app
python run.py
```

Visit `http://127.0.0.1:5000` — you should see the landing page.
Register an account at `/auth/register`, then log in at `/auth/login`.

## Project structure

```
Fitness-Management-System/
├── app/
│   ├── __init__.py        # App factory, extensions, blueprint registration
│   ├── models.py          # User model (role: admin / trainer / client)
│   ├── auth/               
│   │   ├── forms.py        # RegisterForm, LoginForm
│   │   └── routes.py       # /auth/register, /auth/login, /auth/logout
│   ├── main/
│   │   └── routes.py       # / (landing page), /dashboard (placeholder)
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   └── main/
│   └── static/
│       ├── css/style.css
│       ├── js/
│       └── images/
├── config.py
├── run.py
├── requirements.txt
└── .env.example
```

## Notes for next session
- New users all register as `role='client'` for now. Trainer/admin accounts (Kenfit himself,
  and any trainers he adds later) will be created directly in the DB or via an admin-only
  route once we build role management — no public trainer signup.
- `dashboard.html` is a placeholder. In Milestone 3/4 this splits into a real client
  dashboard and trainer dashboard based on `current_user.role`.
- Colour scheme is currently hardcoded to Virgin Active red/black/white in `style.css`.
  Making this dynamic (per Kenfit's request) needs a `Theme`/settings model — planned
  for the theming milestone.
