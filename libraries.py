import math
import datetime

print(math.pi)
print(math.sqrt(81))
print(datetime.datetime.now())

jsondata={"brand":"ford","name":"ram"}
a=json.loads(jsondata)
print(a["brand"])