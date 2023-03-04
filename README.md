
## Requirements ##

Requirements are:

- Python 3
- The Python stuff found in `requirements.txt`
- Javascript stuff managed via [Bower](https://bower.io) - `npm install -g bower`

## Resources used in this project ##

- [Python 3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap](http://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- [django-bower](https://django-bower.readthedocs.io/en/latest/)

## Secrets

A few things are kept in `turnitteal/secrets.py`. (See `secrets.py.example`.)

## Setup for dev/testing ##

### Install requirements ###

If you're using venv, start with this:

```
# This command may be 'python3' or 'python' depending on your system
python -m venv venv
. venv/bin/activate
```

To install everything:

```
python -m pip install -U pip
python -m pip install -r requirements.txt
python manage.py bower install
python manage.py collectstatic
python manage.py migrate
```

(Assumes you have created a `tealdb` database with user `tealdb`
and a password matching `turnitteal/settings.py`.)

You'll need to create a superuser to log in as:

```
python3 manage.py createsuperuser --username dan --email dan@tangledhelix.com
```

And then enter a password twice to set it.

### Update static components ###

To update the version of bower resources, or add more, look at
`BOWER_INSTALLED_APPS` in `settings.py`, then:

```
python manage.py bower install
python manage.py collectstatic
```

For statically-defined resources you manually manage under `{APP}/static`,
manage the file like normal, and then run just the above `collectstatic`
command to assemble all the static resources in one location.

You can call other bower commands similarly, if needed. See here for more
on the django-bower integration:

<https://github.com/nvbn/django-bower>
