from threading import Thread, Event
from time import sleep

from ..schema import ToDo
from ... import socketio

thread_event_stop = Event()

class QueryThread(Thread):
    def __init__(self):
        self.delay = 2
        super(QueryThread, self).__init__()

    def retrieveToDoData(self):
        while not thread_event_stop.isSet():
            print("Retrieving To Do Data")
            result = ToDo().retrieve()
            
            socketio.emit('message',{'data':result}, namespace="/todo-data")
            
            sleep(self.delay)
    
    def run(self):
        self.retrieveToDoData()

