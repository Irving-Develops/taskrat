from flask import Blueprint, request
from app.models import Task, db
from sqlalchemy import desc
from ..forms import TaskForm
from .auth_routes import validation_errors_to_error_messages

task_routes = Blueprint("tasks", __name__ )

@task_routes.route('/')
def all_tasks():
  """ This route returns all available tasks sorted by most recent"""
  tasks = Task.query.order_by(desc(Task.created_at)).filter(Task.available == True).all()
  print(tasks)
  return {"tasks" : [task.to_dict() for task in tasks]}

@task_routes.route('/<int:id>')
def single_task(id):
  """Gets single tasks by their id"""
  task = Task.query.get(id)
  return task.to_dict()

@task_routes.route('/new', methods=["GET", "POST"])
def create_task():

  form = TaskForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    task = Task(
      title = form.data["title"],
      description = form.data["description"],
      city = form.data["city"],
      state = form.data["state"],
      country = form.data["country"],
      price = form.data["price"],
      poster_id = form.data["poster_id"],
      danger_level = form.data["danger_level"]
    )
    db.session.add(task)
    db.session.commit()
    return task.to_dict()

  return { 'errors' : validation_errors_to_error_messages(form.errors) }, 400
