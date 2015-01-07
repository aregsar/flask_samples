def register_blueprints(app):
    from app.views.home import home
    app.register_blueprint(home)

    from app.views.account import account
    app.register_blueprint(account)
