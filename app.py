from flask import Flask, render_template, request
import json
import spacy 
from spacy_client import NamedEntityRecognitionClient

app = Flask(__name__)

ner = spacy.load("en_core_web_sm")
ner = NamedEntityRecognitionClient(ner)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ner',methods=['POST'])
def request_named_entities():
    data = request.get_json()
    result = ner.getEntities(data['sentence'])
    print(result)
    response = {
        "entities":result.get('ents'),
        "html":result.get('html')
        } 
    return json.dumps(response)

if __name__ =='__main__':
    app.run(debug=True)
    
# make sure to run the virtual environment
# conda activate qimono-virtual

# run the server
# python app.py 
