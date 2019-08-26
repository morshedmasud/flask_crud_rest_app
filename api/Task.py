from flask_restful import Resource
import logging as logger

class Task(Resource):

    def get(self):
        logger.debug("get method")
        return {"message": "get method", },200

    def post(self):
        logger.debug("post method")
        return {"message": "post method", }, 200

    def put(self):
        logger.debug("put method")
        return {"message": "put method", }, 200

    def delete(self):
        logger.debug("delete method")
        return {"message": "delete method", }, 200