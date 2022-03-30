from ast import literal_eval
from random import randint
from names_dataset import NameDataset


nameDB = NameDataset()

global gmesg
gmesg = [" is nice", " is naughty", " is Annoying", " is super pushy", " is a pussy", " is very gay, watch out they might try and convert you", " is helpful", " is forgiving", " is crazy", " is energetic", " is funny", " is fabulous", " is not funny"]
global kname
kname = []

def personalityGen(name):
    personalityNum = randint(0,len(gmesg)-1)
    appender(name, personalityNum)
    update()
    print(name + getPersonality(name))
    return(name + getPersonality(name))

def loadFile():
    global kname
    personality1 = open("personality.txt", "r")
    kname = literal_eval(personality1.read())
    personality1.close()

def getPersonality(name):
    return gmesg[kname[kname.index(name)+1]]

def appender(name, personality2):
    kname.append(name)
    kname.append(personality2)

def update():
    personality3 = open("personality.txt", "w")
    personality3.truncate(0)
    personality3.write(str(kname))
    personality3.close()

def checkName(name):
    DB = nameDB.search(name)
    if type(DB.get('first_name')) == type(None):
        return False
    else: 
        return True

def personality(name):
        if checkName(name):
            if name in kname:
                print(1)
                return(name + gmesg[kname[kname.index(name)+1]])
            else:
                print(2)
                return(personalityGen(name))



import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
loadFile()
app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/api/v1/resources/personality', methods=['GET'])
@cross_origin()
def api_personality():
    try:
        
        if 'name' in request.args:
            name = str(request.args['name'])
            print(name)
        else:
            return "Error: No id field provided. Please specify an id."
    except:
        return "Error: No id field provided. Please specify an id."
    print(name)
    print(str(personality(name)))
    return str(personality(name))


app.run(host="0.0.0.0",port = 5000)