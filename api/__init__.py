from flask_restful import Api

from app import app

from .Task import Task
from .TaskById import TaskById


restServer = Api(app)


restServer.add_resource(Task, "/api/task")
restServer.add_resource(TaskById, "/api/task/id/<string:taskId>")