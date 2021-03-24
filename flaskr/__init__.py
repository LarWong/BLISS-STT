import os
from flask import Flask
import requests

def create_app(test_config=None):
    # create and config the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
            )
    if test_config is None:
        # load the instance config
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # This is an endpoint
    @app.route('/')
    def hello():
        # this is just to make sure that it works
        return 'Hello, World!' # RESP: 200 [DEMO]

    @app.route('/speech')
    def speech():
            #Activate DeepSpeech - Assume virtual environment has been created
            #This is an action - this should activate deepspeech
        os.system('python3 mic_vad_streaming.py -m ../deepspeech-0.9.3-models.pbmm')
            #This is the response to a request (GET [default])
            
        return 'DeepSpeech Activated' # RESP: 200 [DEMO]


    return app

if __name__ == "__main__":
    c = create_app()
    c.run()


# TODO
# Request & Reponse cycle
# JSON (JavaScript Object Notation)
# end point triggers -> response: hot word again - use 200
