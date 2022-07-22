# from .db import db
# from .user import User

# class Task(db.Model):
#   __tablename__ = "tasks"

#   id = db.Column(db.Integer, primary_key=True)
#   title = db.Column(db.String(50), nullable=False)
#   description = db.Column(db.Text(2000), nullable=False)
#   city = db.Column(db.String(50), nullable=False)
#   state = db.Column(db.String(50), nullable=False)
#   country = db.Column(db.String(50), nullable=False)
#   price = db.Column(db.Integer, nullable=False)
#   poster_id = db.Column(db.Integer, db.foreignKey("users.id"), nullable=False)
#   tasker_id = db.Column(db.Integer, db.foreignKey("users.id"), nullable=False)
#   danger_level = db.Column(db.Integer, nullable=False)
#   available = db.Column(db.Boolean, nullable=False)
#   completed = db.Column(db.Boolean, nullable=False)
#   created_at = db.Column(db.Timestamp, nullable=False)

#   users = db.relationship(User, back_populates="tasks")


#   def to_dict(self):
#     return {
#       'id': self.id,
#       'title': self.title,
#       'description': self.description,
#       'city': self.city,
#       'state': self.state,
#       'country': self.country,
#       'price': self.price,
#       'poster_id': self.poster_id,
#       'tasker_id': self.tasker_id,
#       'danger_level': self.danger_level,
#       'available': self.available,
#       'completed': self.completed,
#       'created_at': self.created_at
#     }
