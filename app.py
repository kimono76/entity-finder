from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)
    
# make sure to run the virtual environment
# conda activate qimono-virtual

# run the server
# python app.py 
