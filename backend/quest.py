class Quest():
    def __init__(self, id, name, description, reward, latitude, longtitude, username):
        self._name = name
        self._description = description
        self._reward = reward
        self._latitude = latitude
        self._longtitude = longtitude
        self._username = username
        self._in_progress = True
