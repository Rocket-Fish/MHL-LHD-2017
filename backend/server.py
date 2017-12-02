from flask import Flask
from flask import request
from quest import *
import jsonpickle


app = Flask(__name__)
list_of_quests = []
id_to_quest = {}

sample_quest = Quest(0, "Sample Quest", "Testing quests", 5.0, 47.123123, 42.123123, "sampleusername")
list_of_quests.append(sample_quest)

@app.route("/quests/view", methods=['GET'])
def get_quests():
    return jsonpickle.encode(list_of_quests)
    print(request.data)

@app.route("/quests/new", methods=['POST'])
def new_quest():
    


@app.route("/quests/remove", methods=['POST'])
def delete_quest():
    pass
