from flask import Flask, jsonify, request
import app
import logging
from pytz import timezone
from datetime import datetime
import pytz
import time

# Intents:
# "Ok Google, talk to vta bot"
# "Ok Google, talk to vta bot to get schedule"
# "Ok Google, talk to vta bot to get next departure from diridon/school"
# "Ok Google, talk to vta bot to get 2 next departure from diridon/school"
# Google command to update actions.json: ./gactions update --action_package actions.json --project vta-bot
#
# Conversation example with Dash Bus:
# User: Ok Google, talk to vta bot
# Bot: What bus or light rail schedule you'd like to know about?
# User: Dash bus from diridon {mode} and {station}
# Bot: Next 2 departures from {school/diridon} on {dash bus} will occur at 2:40 PM and 2:50 PM
#
# Conversation example with Light rail:
# User: Ok Google, talk to vta bot
# Bot: What bus or light rail schedule you'd like to know about?
# User: Light rail from diridon # {mode} {station}
# Bot: What direction are going?
# User: winchester {station}
# Bot: Next 2 departures from {school/diridon} towards winchester will occur at 2:40 PM and 2:50 PM



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
        log.warning('Message failed to send')
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


@flask.route('/time', methods=['GET','POST'])
def get_time():
    utc_dt = pytz.utc.localize(datetime.utcnow())
    pst_tz = timezone('US/Pacific')
    pst_dt = pst_tz.normalize(utc_dt.astimezone(pst_tz))
    format = '%H%M'
    current_time = pst_dt.strftime(format)
    current_hour = pst_dt.strftime("%H")
    current_minute = pst_dt.strftime("%M")
    result = f"Current time: {current_time}"
    log.info('Time: %s', result)
    return result

@flask.route('/logs', methods=['GET','POST'])
def get_logs():
    return log


# Start the server
if __name__ == '__main__':
    flask.run(debug=True, host='0.0.0.0', port=8080)
