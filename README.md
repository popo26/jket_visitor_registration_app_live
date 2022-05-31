# JKET Parents/Guardians Registration Project

## What is this application?:
###### This application is made for [Japan Kauri Education Trust](http://jket.epizy.com/index.php) in Auckland, New Zealand where they hold a few Japanese classes everyday.At the moment they use a pen and paper when parents drop-off/pick-up their children. This simple application allows JKET admins and parents/guardians to have a central location to record drop-offs/pick-ups as well as to check logs. Even more, they can save the cost of papers!
---

## Technology:
- Django framework
---

## How to run this application:

1. Once clone or download this code, [create a virtualenv](https://docs.python.org/3/library/venv.html).
2. Acticate the virtualenv.
3. From terminal, install all the requirements with `pip install -r requirements.txt`.
4. From terminal, run `python manage.py shell`. Then run below 3 lines of commands to generate a secret key.
 - `from django.core.management.utils import get_random_secret_key`
 - `print(get_random_secret_key())`
 - `exit()`
5. Copy the generated secret key into *settings.py* in *rego* folder, where it says `SECRET_KEY = `. Replace `os.getenv("SECRET_KEY")` with the generated secret key(make sure to put `""`around it).
6. From terminal, run `python manage.py runserver` and go to `127.0.0.1:8000/interaction` to view the landing page.

---

## How to use this application:

### Situation1 --- (Main app) When a parent/guarding drops off/picks up their kid.
- `127.0.0.1:8000/interaction` for landing page.
- Default language is en(English). The second choice is ja(Japanese).
- `127.0.0.1:8000/interaction/classroom_list/` displays only classes happening today.
- Select a particular class to display a list of students.
- Then select a particular student to take the user to the check-in/out page where she is asked to select 2 choices(Drop-off or Pick-up) as well as PIN. (By default **Drop-off** is displayed. Once a class starts, it switches to **Pick-up** after first half of the class time then till 30 min after the class ends.)
- When she forgot her PIN, clicking ***Forgot your PIN?*** link below the PIN field takes to ***JKET PIN Reset Portal*** where she can send a ***PIN reset link*** to her registered email address (uncomment `# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` in settings.py to see the message in the terminal for development environment). Once a new PIN is set via her phone etc., she can go back to the landing page of Registration app by selecting ***Back to Find Child*** link on the app screen. 

### Situation2 --- When a JKET admin staff receives PIN reset request from an user:
- Use ***Lost PIN?*** link in `127.0.0.1:8080/accounts/login/` to send a ***PIN reset link*** to the requester's email.
- Use ***If someone else needs PIN reset, click here*** link in `127.0.0.1:8080/accounts/password_change/` (after the admin person logs into ***JKET PIN Reset Portal***) to send a ***PIN reset link*** to the requester(under development environment you can see it in the terminal as mentioned above).
- Use `127.0.0.1:8000/admin` to reset from the admin portal under User section.

### Situation3 --- When parents and JKET staff want to change PIN.
- Go to `127.0.0.1:8000/accounts/login/` to change their PIN whenever they want.

### Situation4 --- When JKET admin need to administration work.
- Use `127.0.0.1:8000/admin` to add/change student/staff/classroom details as well as view drop-off/pickup logs.


---

## Lastly:
###### JKET is a NPO, therefore I wanted to create this application to save their running cost/menial labour so that they can focus on other things. Introducing PIN and having JKET admin to process user's PIN reset inquiries is my current concern and I tried to smooth out the process. Once I get user feedback I am planning to work on their required usability.
