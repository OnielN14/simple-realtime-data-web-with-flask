from flask import request, jsonify, render_template
from . import main
from .service import ToDoService

@main.route('/')
def home():
    return render_template('index.html',title="Home")

@main.route('/input-todo')
def input_page():
    return render_template('input-page.html',title="Input Page")

@main.route('/todo/store',methods=['POST'])
def store():
    ToDoService().create(request.form.to_dict())
    return "OK"

@main.route('/todo/update/<item_id>',methods=['POST'])
def update(item_id):
    ToDoService().update(item_id,request.get_json())
    return "OK"

@main.route('/todo/delete/<item_id>',methods=['POST'])
def delete(item_id):
    ToDoService().delete(item_id)
    return "OK"

@main.route('/todo',methods=['GET'])
def retrieve():
    return jsonify(ToDoService().retrieve())