from ast import literal_eval
from random import randint

global gmesg
gmesg = [" is nice", " is naughty", " is Annoying", " is super pushy", " is cowardly", " is very happy", " is helpful", " is forgiving", " is crazy", " is energetic", " is funny", " is fabulous", " is not funny", " is clever", " is fun", " is generous"," is loving", " is beautiful"," is aggrovating", " is stupid", " is thoughtful"," is beligerant", " is arrogant", " is conciencous", " is dueplicitcous", " is witty", " is anxious", " is timid", " is shy", " is gullible", " is feeble minded", " is wild", " is complicated", " is loud", " is obnoxius", " is greagrious", " is introverted", " is noxious", " is maciavellian", " is sly", " is goodnatured", " is considarte", " is indepandant", " is gentle", " is amouras", " is cold", " is warm hearted", " is lively", " is slow", " is mendatious", " is quirky", " is sarcastic", " is quirky", " is winsome", " is excentric", " is sexy"]
global kname
kname = []
print(len(gmesg))

def personalityGen(name):
    personalityNum = randint(0,len(gmesg)-1)
    appender(name, personalityNum)
    update()
    print(name + getPersonality(name.lower()))
    return(name + getPersonality(name.lower()))

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
    return True

def personality(name):
        if checkName(name):
            if name.lower() in kname:
                print(1)
                return(name + gmesg[kname[kname.index(name.lower())+1]])
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