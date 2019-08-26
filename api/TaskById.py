from flask_restful import Resource
import logging as logger

class TaskById(Resource):

    def get(self, taskId):
        logger.debug("get method by task id")
        return {"message": "get method by task id. Task-ID = {}".format(taskId)},200

    def post(self, taskId):
        logger.debug("post method by task id")
        return {"message": "post method by task id. Task-ID = {}".format(taskId) }, 200

    def put(self, taskId):
        logger.debug("put method by task id")
        return {"message": "put method by task id. Task-ID = {}".format(taskId) }, 200

    def delete(self, taskId):
        logger.debug("delete method by task id")
        return {"message": "delete method by task id. Task-ID = {}".format(taskId) }, 200