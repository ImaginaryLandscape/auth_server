This module is designed to act as a Basic Auth server.
Active Django Users can be authenticatd against by
performing requests to whereever the auth_moulde url is mounted.

For example, performing the following request will try to authenticate
a user with usernme joe and password 1234.

    curl -v --user "joe:1234" http://localhost:8000/

The response will either be 200 for a successful authentication
or non-200 for a failed authentication.

Middleware on the client side can be designed to make this request.

IMPORTANT: because the passwords and usernames are passed in plain
text, this module should ONLY be hosted under HTTPS.

## NOTES ##

  This module requires:
    django>=1.4
    django-rest-framework
    jsonfield

  The demo directory contains an example django project.

## INSTALLING the MODULE ##

1) Install the this package
    python setup.py install

2) Add the following to INSTALLED_APPS in settings.py

    'rest_framework',
    'auth_server',

3) Add the following to urls.conf

    url(r'^$', include('auth_server.urls')),

4) Run migrate

    ./manage.py migrate


## TESTING the MODULE ##

0) Create a virtualenv and activate if desired

    virtualenv test_demo
    cd test_demo; . ./bin/activate

1) Go to the demo directory

    cd auth_server/demo/

2) Install the requirements

    pip install -r requirements.txt

3) Run the test

    ./manage.py test


## TESTING the MODULE with DOCKER and TOX ##

1) install Docker

2) install docker-compose

3) docker-compose up --build

4) have some coffee
