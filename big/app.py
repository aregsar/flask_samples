from app import app

from config.settings import Settings
app.config.from_object(Settings)

from app.responders.home import home
app.register_blueprint(home)

from app.responders.account import account
app.register_blueprint(account)

print app.url_map

if __name__ == "__main__":
    app.run(debug=True)
