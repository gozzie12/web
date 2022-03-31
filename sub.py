from ast import literal_eval
from random import randint, random
from profanity_filter import ProfanityFilter
pf = ProfanityFilter()
fp = ProfanityFilter()
global gmesg
gmesg = [" is nice", " is naughty", " is Annoying", " is super pushy", " is cowardly", " is very happy", " is helpful", " is forgiving", " is crazy", " is energetic", " is funny", " is fabulous", " is not funny", " is clever", " is fun", " is generous"," is loving", " is beautiful"," is aggrovating", " is stupid", " is thoughtful"," is beligerant", " is arrogant", " is conciencous", " is dueplicitcous", " is witty", " is anxious", " is timid", " is shy", " is gullible", " is feeble minded", " is wild", " is complicated", " is loud", " is obnoxius", " is greagrious", " is introverted", " is noxious", " is maciavellian", " is sly", " is goodnatured", " is considarte", " is indepandant", " is gentle", " is amouras", " is cold", " is warm hearted", " is lively", " is slow", " is mendatious", " is quirky", " is sarcastic", " is quirky", " is winsome", " is excentric", " is sexy"]
global kname
kname = []
print(len(gmesg))
global clname
clname = []
global numname
numname=[]

cl = open("cl.txt", "r")
clname = literal_eval(cl.read())
cl.close()
numer= open("num.txt","r")
numname = literal_eval(numer.read())
numer.close()


def favNum(name):
    if name in numname:
        return numname[numname.index(name)+1]
    else:
        numname.append(name)
        num = randint(1,100)
        numname.append(num)
        updateNum()
        return numname[numname.index(name)+1]

def updateCl():
    cl = open("cl.txt", "w")
    cl.truncate(0)
    cl.write(str(clname))
    cl.close()

def updateNum():
    num = open("num.txt", "w")
    num.truncate(0)
    num.write(str(numname))
    num.close()

def favColour(name):
    if name in clname:
        return clname[clname.index(name)+1]
    else:
        clname.append(name)
        clcode = colourGen()
        clname.append(clcode)
        updateCl()
        return clname[clname.index(name)+1]

def colourGen():
    clcode = hex(randint(0,16777215)).replace("0x","")
    while len(clcode) != 6:
        clcode = "0"+clcode
    return "#"+clcode



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
    name = str(name)
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
    if len(name)>200:
        return "Error: name too long"
    elif name.isnumeric():
        return "Error: do not enter a number"
    print(name)
    print(str(personality(fp.censor(name.replace("#","").lower()))))
    return str(personality(fp.censor(name.replace("#","").lower())))


@app.route('/api/v1/resources/colour', methods=['GET'])
@cross_origin()
def api_colour():
    try:

        if 'name' in request.args:
            name = str(request.args['name'])
            print(name)
        else:
            return "Error: No id field provided. Please specify an id."
    except:
        return "Error: No id field provided. Please specify an id."
    if len(name)>200:
        return "Error: name too long"
    elif name.isnumeric():
        return "Error: do not enter a number"
    print(name)
    print(str(favColour(fp.censor(name.replace("#","").lower()))))
    return str(favColour(fp.censor(name.replace("#","").lower())))

@app.route('/api/v1/resources/num', methods=['GET'])
@cross_origin()
def api_num():
    try:

        if 'name' in request.args:
            name = str(request.args['name'])
            print(name)
        else:
            return "Error: No id field provided. Please specify an id."
    except:
        return "Error: No id field provided. Please specify an id."
    if len(name)>200:
        return "Error: name too long"
    elif name.isnumeric():
        return "Error: do not enter a number"
    print(name)
    print(str(favNum(fp.censor(name.replace("#","").lower()))))
    return str(favNum(fp.censor(name.replace("#","").lower())))