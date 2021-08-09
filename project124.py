from flask import Flask,jsonify,request
app=Flask(__name__)
list=[
    {
        'id': 1,
        'name': u'Saisha',
        'contact': u'614-848-4944',
        'done': False
    },

    {
        'id': 2,
        'name': u'Trupti',
        'contact': u'740-298-3942',
        'done': False
    }
]
@app.route("/")
def helloWorld(): 
    return "Hello World"

@app.route("/add-data",methods=["POST"])
def addTask(): 
    if not request.json: 
        return jsonify({
            "status": "error",
            "message": "Please Provide the Data",
        },400)
    contact={
        'id': list[-1]['id']+1, 
        'name': request.json['name'],
        'contact': request.json.get('contact',""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task Added Successfully"
    })

@app.route("/get-data")
def getTask(): 
    return jsonify({
        "data": tasks
    })

if(__name__=="__main__"): 
    app.run(debug=True)