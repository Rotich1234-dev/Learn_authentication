from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models.dbconfig import db
from models.user import User
from models.passwordresettoken import PasswordResetToken
import cloudinary
import cloudinary.uploader
import jwt
import os
import base64
from werkzeug.security import generate_password_hash, check_password_hash
from flasgger import Swagger
from datetime import datetime, timedelta
from utils import cloudconfig

# swagger -create documentation for our app. uses comment block



app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'Auth and Cloudinary Api Docs',
    'universion': 3
}

swagger = Swagger(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# binding sqlalchemy instance
db.init_app(app)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)