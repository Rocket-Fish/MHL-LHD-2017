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
    longtitude = request.args.get('longtitude')
    print(latitude, longtitude)
    return jsonpickle.encode(get_nearby_quests(latitude, longtitude))


@app.route("/quests/new", methods=['POST'])
def new_quest():
    global counter
    global id_to_quest
    id_to_quest[counter] = Quest(
        request.form.get('name'),
        request.form.get('description'),
        request.form.get('reward'),
        request.form.get('latitude'),
        request.form.get('longtitude'),
        request.form.get('username'))

    counter += 1
    return str(counter - 1)

@app.route("/quests/remove", methods=['POST'])
def delete_quest():
    global id_to_quest
    identity = request.form.get('id')
    del id_to_quest[identity]


def get_nearby_quests(latitude, longtitude):
    return_quests = []
    for identity in id_to_quest:
        quest = id_to_quest[identity]
        (quest_latitude, quest_longtitude) = quest.get_location()
        if (abs(latitude - quest_latitude) <=
                0.01 and abs(longtitude - quest_longtitude) <= 0.01):
            return_quests.append(quest)

    return jsonpickle.encode(return_quests)
