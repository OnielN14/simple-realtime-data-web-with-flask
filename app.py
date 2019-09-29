#!/bin/env python
import eventlet
eventlet.monkey_patch() # Fix IO Block

from simple_app import create_app, socketio
from simple_app.main.schema import Schema

app = create_app(debug=True)

if __name__ == '__main__':
    Schema()
    socketio.run(app)
