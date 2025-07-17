from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()
app= Flask(__name__)
CORS(app)

#app.config['DEBUG']=os.environ.get('FLASK_DEBUG')

@app.route('/')
def hello_world():
    return "hello word"

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    app.run()
