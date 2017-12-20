from flask import Flask, jsonify, request
import app
import logging

# Intents:
# "Ok Google, talk to Dash Bus"
# "Ok Google, talk to Dash Bus to get schedule"
# "Ok Google, talk to Dash Bus to get next departure from diridon/school"
# "Ok Google, talk to Dash Bus to get 2 next departure from diridon/school"
# Google command to update actions.json: ./gactions update --action_package actions.json --project dashbot-f965e


# Flask setup
flask = Flask(__name__)
flask.config['ASSIST_ACTIONS_ON_GOOGLE'] = True

# Logger setup
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


@flask.route('/assistant', methods=['GET', 'POST'])
def assist():
    """Receive JSON request from Google Assistant device, create response and send it back"""

    content = request.get_json()  # Get raw JSON
    query = content['inputs'][0]['rawInputs'][0]['query']  # JSON parsing to get the query
    tokens = app.tokenize(query)  # NLP
    response = app.construct_response(tokens)  # Check if there is a response

    if response:  # If the response was constructed
        log.info('Message sent: ' + response)
        return construct_json(response)
    elif response is None:
        log.debug('Message failed to send')
        return construct_json("I don't get that yet!")


# Create a JSON constructor to respond to Google Assistant
def construct_json(message):
    """Returns a reply back to Google Assistant in the correct JSON format.
    JSON follows API 2 of Google Actions SDK"""

    response = {
        "conversationToken": "",
        "expectUserResponse": True,
        "expectedInputs": [
            {
                "inputPrompt": {
                    "richInitialPrompt": {
                        "items": [
                            {
                                "simpleResponse": {
                                    "textToSpeech": message,
                                    "displayText": message
                                }
                            }
                        ],
                    }
                },
                "possibleIntents": [
                    {
                        "intent": "actions.intent.TEXT"
                    }
                ]
            }
        ],
    }
    return jsonify(response)


# Start the server
if __name__ == '__main__':
    flask.run(debug=True, host='0.0.0.0', port=5000)
