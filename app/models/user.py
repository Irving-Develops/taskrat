from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(75), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    pic_url = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.String(2000), nullable=True)


    tasks = db.relationship('Task', back_populates="users")


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'pic_url': self.pic_url,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'bio': self.bio,
        }


class Task(db.Model):
  __tablename__ = "tasks"

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50), nullable=False)
  description = db.Column(db.String(2000), nullable=False)
  city = db.Column(db.String(50), nullable=False)
  state = db.Column(db.String(50), nullable=False)
  country = db.Column(db.String(50), nullable=False)
  price = db.Column(db.Integer, nullable=False)
  poster_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
  tasker_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
  danger_level = db.Column(db.Integer, nullable=False)
  available = db.Column(db.Boolean, nullable=False)
  completed = db.Column(db.Boolean, nullable=False)
  created_at = db.Column(db.Date, nullable=False)

  users = db.relationship('User', back_populates="tasks")


  def to_dict(self):
    return {
      'id': self.id,
      'title': self.title,
      'description': self.description,
      'city': self.city,
      'state': self.state,
      'country': self.country,
      'price': self.price,
      'poster_id': self.poster_id,
      'tasker_id': self.tasker_id,
      'danger_level': self.danger_level,
      'available': self.available,
      'completed': self.completed,
      'created_at': self.created_at
    }
