from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

import logging as logger
logger.basicConfig(level="DEBUG")


# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)



# Task Class/Model
class Tasks(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  task = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))


  def __init__(self, task, description):
    self.task = task
    self.description = description



class TasksSchema(ma.Schema):
  class Meta:
    fields = ('id', 'task', 'description')


# Init schema
task_schema = TasksSchema()
tasks_schema = TasksSchema(many=True)


# Create a Task
@app.route('/app', methods=['POST'])
def add_task():
  task = request.json['task']
  description = request.json['description']


  new_task = Tasks(task, description)

  db.session.add(new_task)
  db.session.commit()

  return task_schema.jsonify(new_task)

# Get All Tasks
@app.route('/app', methods=['GET'])
def get_tasks():
  all_tasks = Tasks.query.all()
  result = tasks_schema.dump(all_tasks)
  return jsonify(result)


# Update a Tasks
@app.route('/app/<id>', methods=['PUT'])
def update_task(id):
  tasks = Tasks.query.get(id)

  task = request.json['task']
  description = request.json['description']


  tasks.task = task
  tasks.description = description


  db.session.commit()

  return task_schema.jsonify(tasks)


# Delete Task
@app.route('/app/<id>', methods=['DELETE'])
def delete_task(id):
  task = Tasks.query.get(id)
  db.session.delete(task)
  db.session.commit()

  return task_schema.jsonify(task)


if __name__ == '__main__':
    logger.debug("Starting the application")
    app.run(debug=True, use_reloader=True)