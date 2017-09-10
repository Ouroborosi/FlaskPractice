#!flask/bin/python
from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def show_tasks():
    return jsonify({'tasks': tasks})

@app.errorhandler(404)
def _404Handler():
    return jsonify({'error': 'Not found'}), 404

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if not task:
        return _404Handler()
    return jsonify({'task': task[0]})

def fn(task_id):


    return task_id
if __name__ == '__main__':
    app.run(debug=True)