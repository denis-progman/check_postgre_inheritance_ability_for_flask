from datetime import timedelta
from db import db, migrate
from flask import Flask
from configs import current_config 
from router import routs_init
from flask_session import Session


app_instance = Flask(__name__)
app_instance.config.from_object(current_config)
db.init_app(app_instance)
migrate.init_app(app_instance, db)

app_instance.config["SESSION_TYPE"] = "filesystem"
app_instance.config["SECRET_KEY"] = "SDALFKHksdzjfnadsfnj65168"
app_instance.permanent_session_lifetime = timedelta(minutes=5)

if __name__ == "__main__":
    app_instance.run()

routs_init(app_instance)
