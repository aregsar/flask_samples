from app import app

#load configuration
from app.config.settings import Settings
app.config.from_object(Settings)

#register route blueprints
from app.responders.home import home
app.register_blueprint(home)

from app.responders.account import account
app.register_blueprint(account)

print app.url_map

#run the app
if __name__ == "__main__":
    app.run(debug=True)
