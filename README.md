
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

## Setup for dev/testing ##

### Install requirements ###

```
pyvenv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py bower install
python3 manage.py collectstatic
```

### Update static components ###

To update the version of bower resources, or add more, look at
`BOWER_INSTALLED_APPS` in `settings.py`, then:

```
python3 manage.py bower install
python3 manage.py collectstatic
```

For statically-defined resources you manually manage under `{APP}/static`,
manage the file like normal, and then run just the above `collectstatic`
command to assemble all the static resources in one location.

You can call other bower commands similarly, if needed. See here for more
on the django-bower integration:

<https://github.com/nvbn/django-bower>