# django-track-engine-api

A backend API for tracking engineering issues. Engineers report bugs, assign priorities, and track status — basically a stripped-down take on something like GitHub Issues.

---

## how i run this locally

From the project root (where `manage.py` lives):

```bash
python3 -m venv .venv
source .venv/bin/activate   # on windows: .venv\Scripts\activate
pip install -r requirement.txt
python manage.py migrate
python manage.py runserver
```

Then the API is at `http://127.0.0.1:8000/` (Django default). All the issue/reporter routes sit under `/api/`.

If something fails on install, make sure you're on a recent Python 3 — this project was set up with Django 6.

---

## what the endpoints actually do

Base path is **`/api/`** (see `devtrack/urls.py`).

### Issues — `/api/issues/`

- **GET** with no query params — returns every issue from the JSON store.
- **GET** `?id=<number>` — one issue by id. 404 if it doesn’t exist.
- **GET** `?status=<whatever>` — filter issues where `status` matches (e.g. open, closed — whatever you’ve saved).
- **POST** — create a new issue. Body is JSON with fields like `id`, `title`, `description`, `status`, `priority`, `reporter_id`, `created_at`. If you send `priority` as `high`, `medium`, or `low`, the backend picks a slightly different “shape” of issue so the description text in the response reflects that priority; anything else falls back to the base issue type.

### Reporters — `/api/reporters/`

- **GET** with no params — list all reporters.
- **GET** `?id=<number>` — one reporter. 404 if missing.
- **POST** — add a reporter (`id`, `name`, `email`, `team` in the body). It validates name and a basic email check before appending.

### Admin (optional)

- **`/admin/`** — Django admin if you’ve created a superuser (`python manage.py createsuperuser`).

---

## one design choice i stuck with (and why)

I’m **not using the ORM for issues and reporters** — they’re plain Python objects and everything goes to **`issues.json`** and **`reporters.json`**. Reason is pretty boring but honest: for this assignment I wanted the data model and API behavior in one place without fighting migrations and serializers for every field change. You can open the JSON files and see exactly what got stored. Downside is it’s not great for production (no real concurrency, paths, etc.), but for learning and iterating fast it worked for me.

---

If anything here drifts from the code, trust the code — this is just how I remember running and using it.



Screenshot of Enpoints tested in Postman

1. Get All Issues
