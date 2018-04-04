import json


f = open("test.json","r",encoding="UTF-8")
x = json.load(f)
f.close()
print(x)