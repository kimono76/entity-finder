from crypt import methods
import json
from urllib import response
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ner',methods=['POST'])
def request_named_entities():
    data = request.get_json()
    response = True 
    return json.dumps(response)

if __name__ =='__main__':
    app.run(debug=True)
    
# make sure to run the virtual environment
# conda activate qimono-virtual

# run the server
# python app.py 
