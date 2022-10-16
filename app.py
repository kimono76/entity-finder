from flask import Flask, render_template, request
import json
import spacy
from spacy_client import NamedEntityRecognitionClient
from public_ip_handler import public_ip
from flask_cors import CORS

app = Flask(__name__)

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
