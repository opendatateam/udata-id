# Binding for [id.data.gouv.fr](https://github.com/etalab/id.data.gouv.fr) and [uData](https://github.com/etalab/id.data.gouv.fr)

_udata-id_ binds the OAuth2 SSO [id.data.gouv.fr](https://github.com/etalab/id.data.gouv.fr) into the [udata](https://github.com/opendatateam/udata) project.


## Prerequiments

- an installation of [uData](https://github.com/opendatateam/udata) and of
[id.data.gouv.fr](https://github.com/etalab/id.data.gouv.fr) properly running.
- a _client\_id_ and a _client\_secret_ from _id.data.gouv.fr_ (see the next
chapter for setting up these OAuth settings).


## Setting up the OAuth

We will setup an OAuth2 to connect with the following parameters:

- **Authorization Grant Type:** _authorization-code_
- **client type:** _public_
- **redirect url:** _http://localhost:5000/complete/id_ (adapt to your _uData_
  domain)

While running _id.data.gouv.fr_ (eg: `./manage.py runserver`):

1. go to http://localhost:8000/oauth/applications/register/,
2. fill the form with the parameter given above,
3. keep your _client\_id_ and _client\_secret_, you will need them for the
configuration.


## Installation

    git clone https://github.com/opendatateam/udata-id.git

The project being used by _uData_, ensure that the _udata\_id_ package is
available from your _udata_ project's _virtualenv_ (eg: `add2virtualenv /path/to/my/udata-id`).

activate your **_udata_ virtualenv** (eg: `source /path/to/udata/venv/bin/activate`) and install the _udata-id_ requirements within it:

    pip install -r requirements.txt

_udata-id_ depends on [Python Social Auth]; add this plugin's settings to your
uData config (_udata.cfg_) and adapt _social auth_ (installed with requirements)
config to connect to it:

    PLUGINS = […, 'id']
    SOCIAL_AUTH_STORAGE = 'social.apps.flask_app.me.models.FlaskStorage'
    SOCIAL_AUTH_USER_MODEL = 'udata.core.user.models.User'
    SOCIAL_AUTH_ID_KEY = 'my_client_id'  # client_id from above
    SOCIAL_AUTH_ID_SECRET = 'my_id_secret'  # client_secret from above
    SOCIAL_AUTH_AUTHENTICATION_BACKENDS = ('udata_id.backends.IDOAuth2',)
    USERNAME_IS_FULL_EMAIL = True

You're all set!
Now if you browse on your _uData_ installation and click on _login / register_,
you should be redirected to your _id.data.gouv.fr_ server and authenticate from
there.
