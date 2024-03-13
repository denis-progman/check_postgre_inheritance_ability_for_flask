import datetime
import os

from db import db, migrate
from flask import Flask
from configs import current_config
from router import routs_init

app_instance = Flask(__name__)
app_instance.config.from_object(current_config)
db.init_app(app_instance)
migrate.init_app(app_instance, db)

# Session data
s_key = os.urandom(20).hex()
app_instance.config['SECRET_KEY'] = s_key
# default time is 31 days(app.permanent_session_lifetime)
app_instance.permanent_session_lifetime = datetime.timedelta(days=10)

if __name__ == '__main__':
    app_instance.run()

routs_init(app_instance)