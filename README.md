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
<img width="1500" height="998" alt="image" src="https://github.com/user-attachments/assets/39562d11-61ce-4220-8b22-1e765d7453b8" />

2. Get issue by Id (Success)
<img width="1021" height="733" alt="image" src="https://github.com/user-attachments/assets/e4770c25-b02d-4c42-86d4-4e04d4af78b5" />

3. Get issue by id (Fail)
<img width="1021" height="759" alt="image" src="https://github.com/user-attachments/assets/d6fff13b-e956-4a00-acf3-b6f3b4dca22c" />

4. Get issue by status
<img width="1022" height="760" alt="image" src="https://github.com/user-attachments/assets/5f5bc44f-239c-459a-942e-c1091d65cffa" />

5. Create a reported
<img width="1020" height="756" alt="image" src="https://github.com/user-attachments/assets/0a074a5f-4fdd-4716-bc73-53020024695f" />

6. Get reporter by id (Success)
<img width="1015" height="755" alt="image" src="https://github.com/user-attachments/assets/aec12b43-fdec-4c15-8d3e-78afcca02880" />

7. Get reporter by id (Fail)
<img width="1020" height="758" alt="image" src="https://github.com/user-attachments/assets/9da711b1-81d9-4e19-ab26-23ef5179b25c" />





