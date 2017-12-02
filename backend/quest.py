import datetime

class Quest():
    def __init__(self, name, description, reward, latitude, longtitude, username):
        self._name = name
        self._description = description
        self._reward = reward
        self._latitude = latitude
        self._longtitude = longtitude
        self._username = username
        self._in_progress = True
        self._time_created = str(datetime.datetime.now())

    def get_location(self):
        return (self._latitude, self._longtitude)
