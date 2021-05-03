import os
from flask import Flask, Response, request
import requests
from vui_deepspeech import *
from vui_wakeword import *
import sounddevice as sd
import json
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

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
    
    stt_model = STTModel(model='deepspeech-0.9.3-models.pbmm', scorer='deepspeech-0.9.3-models.scorer')

    synthesizer = torch.hub.load('coqui-ai/TTS:dev', 'tts', source='github')

    def speak(output_text):
        wav = synthesizer.tts(output_text)
        sd.play(wav, synthesizer.ap.sample_rate)
        sd.wait()

    @app.route('/speech')
    def speech():
        # Activate DeepSpeech - Assume virtual environment has been created
        # This is an action - this should activate deepspeech

        # Say how may i help you
        speak('How may I help you?')
        # print("Diego Says: How may I help you?")

        # Listen for speech
        text = stt_model.run()
        # print("User Says: " + str(text))

        return text

    @app.route('/nlp')
    def nlp():
        # Activate DeepSpeech - Assume virtual environment has been created
        # This is an action - this should activate deepspeech

        print("HEEREREE")

        text = request.json['text']

        # Send to rasa
        payload = {
            'sender':'test',
            'message':text
        }
        headers = {
            'content-type': 'application/json'
        }
        # Send it over to RASA
        response_rasa = requests.post('http://localhost:5005/webhooks/rest/webhook', json = payload, headers = headers)

        print(response_rasa.json())

        feedback = json.loads(response_rasa.content) if response_rasa else 'Sorry, I could not reach the server. Please try again'

        print("Diego Says: " + str(feedback[0]['text']))

        speak(feedback[0]['text'])

        resp = {
            'messages': feedback
        }

        return resp # RESP: 200 [DEMO]

    # This checks the status of the server
    @app.route('/status')
    def status():
        # this is just to make sure that it works
        return 'OK' # RESP: 200 [DEMO]

    return app

if __name__ == "__main__":
    c = create_app()
    c.run()


# TODO
# Request & Reponse cycle
# JSON (JavaScript Object Notation)
# end point triggers -> response: hot word again - use 200
