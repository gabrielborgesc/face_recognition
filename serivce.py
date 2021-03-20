import json
import numpy as np
import dao

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def npArrayToJson(npArray):
    json_dump = json.dumps(npArray, cls=NumpyEncoder)
    return json_dump

def jsonToNpArray(json_array):
    json_load = json.loads(json_array)
    npArray = np.asarray(json_load)
    return npArray

def findUser(encodings):
    userList = dao.get_all_users()
    difArray = []
    minDifference = 1
    for user in userList: # each user is a tuple
        userArray = jsonToNpArray(user[2])
        dif = np.linalg.norm(encodings-userArray)
        if(dif <= minDifference):
            minDifference = dif
            closestUser = user
    if(minDifference <= 0.4): # same face
        return closestUser
    return None