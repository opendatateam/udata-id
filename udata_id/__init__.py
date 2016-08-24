from flask import current_app, g, request, redirect
from social.apps.flask_app.routes import social_auth
from social.apps.flask_app.me.models import init_social

from udata.auth import current_user
from udata.core.user.models import User
from udata.models import db


def init_app(app):
    app.register_blueprint(social_auth)
    init_social(app, db)

    @app.before_request
    def global_user():
        g.user = current_user

    @app.login_manager.user_loader
    def load_user(userid):
        try:
            return User.objects.get(id=userid)
        except (User.DoesNotExist):
            return None

    @app.context_processor
    def inject_user():
        '''Make current user available on templates'''
        try:
            return {'user': g.user}
        except AttributeError:
            return {'user': None}

    def redirect_login():
        url = '{url}?next={next}'.format(url=app.config.get('LOGIN_URL', '/'),
                                         next=request.args.get('next', ''))
        return redirect(url)

    # Hacking security login URL, inspired from previous 'Youckan'. Improve me!
    app.view_functions['security.login'] = redirect_login
