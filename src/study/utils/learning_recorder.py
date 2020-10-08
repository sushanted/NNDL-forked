import json

def record(filename,value):
    with open(filename,"a") as outfile:
        outfile.write(json.dumps(value)+'\n')



