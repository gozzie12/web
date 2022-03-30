from ast import literal_eval
from random import randint
from names_dataset import NameDataset
import sys


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

def printer(mesg):
    print(mesg)
    error(mesg)

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

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

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


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    try:
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."
    except:
        return "Error: No id field provided. Please specify an id."

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)

app.run(host="0.0.0.0",port = 5000)