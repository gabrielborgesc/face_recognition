import json
import numpy as np
import serivce

a = np.array([1, 2, 3])
print('nparray', a)

json_dump = serivce.npArrayToJson(a)
print('jsonArray', json_dump)

json_load = json.loads(json_dump)
a_restored = np.asarray(json_load)
print('np_restored', a_restored)