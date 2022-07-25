from flask import Blueprint
from app.models import Task
from sqlalchemy import desc

task_routes = Blueprint("tasks", __name__ )

@task_routes.route('/')
def all_tasks():
  """ This route returns all available tasks sorted by most recent"""
  tasks = Task.query.order_by(desc(Task.created_at)).filter(Task.available == True).all()
  print(tasks)
  return {"tasks" : [task.to_dict() for task in tasks]}
