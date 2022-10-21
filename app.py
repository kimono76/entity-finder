from flask import Flask, render_template, request, Blueprint
import json
import spacy
from spacy_client import NamedEntityRecognitionClient
from public_ip_handler import public_ip
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)

main = Blueprint('main',__name__)
app.register_blueprint(main)

app.config['MONGO_URI'] = 'mongodb+srv://qimono:Secret-Ento-76@cluster0.jlga6l0.mongodb.net/DbEnto?retryWrites=true&w=majority'

# Collection name = NamedEntities

mongodb_client = PyMongo(app)
db = mongodb_client.db

named_entities_collection = db.NamedEntities


CORS(app)

ner = spacy.load("en_core_web_sm")
ner = NamedEntityRecognitionClient(ner)

@app.route('/')
def index():
    public_ip.get_ip()
    return render_template('index.html')

@app.route('/ner',methods=['POST'])
def request_named_entities():
    data = request.get_json()
    print('data = ')
    print(data)
    result = ner.getEntities(data['sentence'])
    print(result)
    response = {
        "entities":result.get('ents'),
        "html":result.get('html')
        }
    return json.dumps(response)


@app.route('/sample', methods=['GET'])
def request_sample_entities():
    result = ner.getEntities('George Washington was the first president of USA')
    print(result)
    
    # named_entities_collection.insert_one({
    #     'ent':'George Washington',
    #     'label':'person',
    #     'correction-label':'',
    #     'cetified':True,
    # })
    
    #response = {"entities": result.get('ents'), "html": result.get('html')}
    return result #json.dumps(response)

if __name__ =='__main__':
    app.run(
        #host='127.0.01',
        host='0.0.0.0',
        #host='192.168.0.110',
        #host=public_ip.get_ip(),
        port=3000,
        debug=True)
    #app.run(debug=True)

# make sure to run the virtual environment
# conda activate qimono-virtual

# run the server
# python app.py

# to allow cross origin resource sharing you must install flask-from
# pip install -U flask-cors

# to support MongoDb in flask
# pip install Flask-PyMongo
# dnspython is needed
# python -m pip install "pymongo[srv]"
# pip install pythondns
