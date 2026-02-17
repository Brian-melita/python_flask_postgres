from flask import Flask

from models.dbconnection import db
from flask_migrate import Migrate
from models.deals_items import DealsItems

app = Flask(__name__)
app.config.from_prefixed_env()
# CONNECT TO DATABASE SERVER
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:melitah@localhost:5432/deals_db"

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return "Welcome to Moringa"

@app.route('/about/<string:username>')
def about(username):
    return f"Welcome {username} to Moringa School" 