# Server setup #

How I deployed this thing to a server.

In this case it was Ubuntu 16.04.1 x64.

## The usual ##

First I did the usual in a root login.

```
~/.ssh/config:
Host db.turnitteal.org
    User root
    IdentityFile ~/.ssh/digitalocean
```

Initial setup steps:

```
apt-get update && apt-get upgrade
apt-get upgrade

apt-get install git zsh
useradd -s /bin/zsh -c 'Dan Lowe' -m dan

visudo              ## Give dan sudo juice.
passwd dan          ## Set a sudo password for dan.

mkdir ~dan/.ssh
cp /root/.ssh/authorized_keys ~dan/.ssh
chown -R dan:dan ~dan/.ssh
chmod 700 ~dan/.ssh
chmod 600 ~dan/.ssh/authorized_keys

vi /etc/ssh/sshd_config
    ## Port 2914
    ## PermitRootlogin no
    ## PasswordAuthentication no
systemctl restart sshd.service

ufw allow 2914
ufw enable
```

Now make sure dan can ssh in and sudo. After that, close the original root ssh
window. Check that `ufw status` allows 2914 and nothing else.

New ssh config:

```
Host db.turnitteal.org
    User dan
    IdentityFile ~/.ssh/digitalocean
    Port 2914
```

Reboot, then ssh back in as dan.

Verify `ufw status` still has the 2914 rule present.

```
git clone git@github.com:tangledhelix/dotfiles .dotfiles
cd .dotfiles
./install.pl all
```

## App requirements ##

Doing this as a virtualenv. Make sure Python 3 stuff is installed.

```
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv python3-wheel
sudo pip3 install uWSGI
```

This project used Bower stuff, so let's install node and bower.

```
sudo apt-get install nodejs npm
sudo ln -s /usr/bin/nodejs /usr/bin/node
sudo npm install -g bower
```

And we need postgres running.

```
sudo apt-get install postgresql libpq-dev
```

## Set up database ##

```
sudo su - postgres
createuser -s dan
exit
createdb tealdb
## Get the password from the Django settings.py
psql -d tealdb -c "CREATE USER tealdb WITH PASSWORD 'foo'"
```

## Set up application ##

```
git clone git@github.com:tangledhelix/tealdb
cd tealdb
pyvenv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py bower install
python manage.py collectstatic
```

If the hostname has changed, you may need to add it to the `ALLOWED_HOSTS`
array in `turnitteal/settings.py`.

## Add a WSGI service ##

```
sudo mkdir -p /etc/uwsgi/sites
cd /etc/uwsgi/sites
```

New file `tealdb.ini` with these contents:

```
[uwsgi]

chdir = /home/dan/tealdb
home = /home/dan/tealdb/venv
module = turnitteal.wsgi:application

master = true
processes = 5

socket = /tmp/turnitteal.sock
chmod-socket = 666
vacuum = true
```

Now we set up a service definition.

```
cd /etc/systemd/system
```

New file: `uwsgi.service` with these contents:

```
[Unit]
Description=uWSGI Emperor service
After=syslog.target

[Service]
ExecStart=/usr/local/bin/uwsgi -H /home/dan/tealdb/venv --emperor /etc/uwsgi/sites
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

Activate the service, and set it to run on boot.

```
sudo systemctl start uwsgi.service
sudo systemctl enable uwsgi.service
```

Now look at status, it should be running, and enabled.

```
sudo systemctl enable uwsgi.service
```

## Nginx and Let's Encrypt ##

```
sudo git clone https://github.com/letsencrypt/letsencrypt /opt/letsencrypt
sudo apt-get install nginx
sudo ufw allow 80                ## This is only here for letsencrypt.
sudo ufw allow 443
sudo /opt/letsencrypt/letsencrypt-auto certonly -a webroot \
    --webroot-path=/var/www/html -d db.turnitteal.org
```

Saved to: `/etc/letsencrypt/live/db.turnitteal.org/fullchain.pem`.

Set up a cron job to auto-renew it later.

```
cd /etc/cron.d
```

New file `letsencrypt` with these contents.

```
30 2 * * 1 root /opt/letsencrypt/letsencrypt-auto renew >> /var/log/le-renew.log
35 2 * * 1 root /bin/systemctl reload nginx
```

Digital Ocean tutorial suggested this for strong DH group...
This will take a while, especially on a small droplet.

```
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
```

Set up the password file.

```
cd /etc/nginx
sudo touch htpasswd
sudo chown root:www-data htpasswd
sudo chmod 640 htpasswd
```

`htpasswd` should have these contents:

```
steph:RGpTRE0gUpeQU
dan:39AVuFLULM/SQ
```

Now configure nginx with the new virtualhost.

```
cd /etc/nginx/sites-available
```

New file `tealdb` with these contents:

```
server {
    listen 443 ssl;
    listen [::]:443 ssl;

    # Note: You should disable gzip for SSL traffic.
    # See: https://bugs.debian.org/773332
    #
    # Read up on ssl_ciphers to ensure a secure configuration.
    # See: https://bugs.debian.org/765782

    ssl_certificate /etc/letsencrypt/live/db.turnitteal.org/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/db.turnitteal.org/privkey.pem;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name db.turnitteal.org;

    auth_basic "Authentication required";
    auth_basic_user_file htpasswd;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /home/dan/tealdb;
    }

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/tmp/turnitteal.sock;
    }

}
```

Now activate it:

```
cd /etc/nginx/sites-enabled
sudo ln -s ../sites-available/tealdb
sudo systemctl restart nginx.service
```

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
pip install --upgrade pip
pip install -r requirements.txt
python manage.py bower install
python manage.py collectstatic
python manage.py migrate
```

(Assumes you have created a `tealdb` database with user `tealdb`
and a password matching `turnitteal/settings.py`.)

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
