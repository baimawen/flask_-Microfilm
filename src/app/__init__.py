# coding: utf8



from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
import pymysql
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:rw@mysql-data:3306/movie"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "4fa7d311c0eb4f7b88fdee479f24391d"
app.config['REDIS_URL'] = "redis://:123456@myredis:6379/0"
app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")
app.debug = False
db = SQLAlchemy(app)
rd = FlaskRedis(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")

# 404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
