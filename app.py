from flask import Flask,jsonify, request

# This is like a constructor off the class flask. It takes the name of the current module.
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

# route() of Flask is like a decorator which will tell our web app which url is associated with it (the function too). 
@app.route("/")
def hello_world():
    return "Hello World!"

# We are specifying what we want to have on the root. 
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    
# If we run this, we will see all the tasks we gave at the top.
@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

# To run the code on our web application, we can say app.run(). To say the next changes, we added "debug=True". 
if (__name__ == "__main__"):
    app.run(debug=True)