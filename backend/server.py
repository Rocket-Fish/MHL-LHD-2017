from flask import Flask
from flask import request
from quest import *
import jsonpickle

app = Flask(__name__)
id_to_quest = {}
counter = 0

@app.route("/quests/view", methods=['GET'])
def get_quests():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    print(latitude, longitude)
    return jsonpickle.encode(get_nearby_quests(float(latitude), float(longitude)))


@app.route("/quests/new", methods=['POST'])
def new_quest():
    global counter
    global id_to_quest
    id_to_quest[counter] = Quest(
        str(request.form.get('name')),
        str(request.form.get('description')),
        float(request.form.get('reward')),
        float(request.form.get('latitude')),
        float(request.form.get('longitude')),
        str(request.form.get('username')))
        
    counter += 1
    return str(counter - 1)

@app.route("/quests/remove", methods=['POST'])
def delete_quest():
    global id_to_quest
    identity = request.form.get('id')
    del id_to_quest[identity]


def get_nearby_quests(latitude, longitude):
    return_quests = []
    global id_to_quest
    for identity in id_to_quest:
        quest = id_to_quest[identity]
        (quest_latitude, quest_longitude) = quest.get_location()
        if (abs(latitude - quest_latitude) <=
                0.01 and abs(longitude - quest_longitude) <= 0.01):
            return_quests.append(quest)

    return return_quests
