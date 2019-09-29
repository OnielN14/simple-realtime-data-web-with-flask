from threading import Thread
from flask_socketio import emit
from .async_job.QueryThread import QueryThread

from .. import socketio

@socketio.on('connect', namespace="/todo-data")
def join():
    thread = socketio.start_background_task(target=QueryThread().retrieveToDoData)