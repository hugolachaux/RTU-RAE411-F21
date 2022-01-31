
import flask as fs
import requests, json
from flask import request, jsonify



def n_num_getter(scores, n):
    return list(scores)[n]

app = fs.Flask(__name__)
app.config["DEBUG"] = True


url = "https://4v9r83qfo4.execute-api.eu-central-1.amazonaws.com/dev"

response = requests.get(url)

myData = json.loads(response.text);



### We generate a get method 
@app.route('/', methods=['GET'])
def all_data():
    return jsonify(myData)



### We generate a new web page 
@app.route('/courseName', methods=['GET'])
def courseName_data():
        return jsonify(myData["courseName"])



@app.route('/newJson', methods=['POST'])
def add_score():

    info = {'devise' : request.json["hello world"]}

    myData.append(info)

    return jsonify(myData)



### We generate a new request 
@app.route('/scores/<int:n>', methods=['DELETE'])

def score_delete(n):
    index = n_num_getter(data["scores"], n)    
    if (index != "Not so much scores yet!"):
        
        to_return = {index: (data["scores"])[index]}
        (myData["scores"]).pop(index)
        return jsonify(to_return)
    
    else:
        
        return ("Invalid Index")




app.run()
