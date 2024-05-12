from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models.dbconfig import db
from models.user import User
from models.passwordresettoken import PasswordResetToken

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)