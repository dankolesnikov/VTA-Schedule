import random
import nltk
import time
from flask import Flask, jsonify, request

# Intents:
# "Ok Google, talk to Dash Bus"
# "Ok Google, talk to Dash Bus to get schedule"
# "Ok Google, talk to Dash Bus to get next departure from diridon"
# "Ok Google, talk to Dash Bus to get 2 next departure from diridon"
# Google command to update actions.json: ./gactions update --action_package actions.json --project dashbot-f965e


# Flask & Google Assistant stuff
app = Flask(__name__)
app.config['ASSIST_ACTIONS_ON_GOOGLE'] = True

# Setting up time data
currentTime = time.strftime("%I:%M")
currentHour = time.strftime("%I")
currentMinute = time.strftime("%M")
ampm = time.strftime("%p")
isWeekend = False
print("Current time is: " + currentHour + ampm)

# Check is today is a weekend
if time.strftime("%w") is "0" or time.strftime("%w") == "6":
    isWeekend = True


# Keywords for NLP later
GREETING_KEYWORDS = ("hello", "hi", "greetings", "hey", "whats up", "talk to dash bus")
GREETING_RESPONSES = ["Hey commuter!", "Hello commuter!"]
ACTIVATION_RESPONSES_DIRIDON = ["schedule", "get schedule", 'talk to dash bus to get schedule']


# Map corresponding values
# From Diridon Station
timeScheduleFromDiridon = {}
timeScheduleFromDiridon["06AM"] = ['34','51']
timeScheduleFromDiridon["07AM"] = ['06','14','23','30','40','48','52']
timeScheduleFromDiridon["08AM"] = ["03","09","16","24","35","40","47","50"]
timeScheduleFromDiridon["09AM"] = ["09","16","24","40","47"]
timeScheduleFromDiridon["10AM"] = ["02","16","30","45"]
timeScheduleFromDiridon["11AM"] = ["01", "17", "31", "45"]
timeScheduleFromDiridon["12PM"] = ["00","15","30","45"]
timeScheduleFromDiridon['1PM']  = ["02","19", "34", "49"]
timeScheduleFromDiridon['2PM']  = ["06","23", "40", "49"]
timeScheduleFromDiridon['3PM']  = ["07","16", "29", "40",'46','56']
timeScheduleFromDiridon['4PM']  = ["06","12", "18", "28",'38','48','58']
timeScheduleFromDiridon['5PM']  = ["04","14", "23", "30",'39','51']
timeScheduleFromDiridon['6PM']  = ["06","22", "48", "22",'48']
timeScheduleFromDiridon['7PM']  = ["22", "47"]
timeScheduleFromDiridon['8PM']  = ["15", "34"]
timeScheduleFromDiridon['9PM']  = ["11"]

# From SJSU Campus
timeScheduleFromSchool = {}
timeScheduleFromSchool["06AM"] = ['41','58']
timeScheduleFromSchool["07AM"] = ['13','21','38','48','56']
timeScheduleFromSchool["08AM"] = ['00','11','17','24','32','43','48','55']
timeScheduleFromSchool["09AM"] = ['04','17','24','32','47','54']
timeScheduleFromSchool["10AM"] = ['09','23','37','52']
timeScheduleFromSchool["11AM"] = ['08','24','38','52']
timeScheduleFromSchool["12PM"] = ['07','22','37','52']
timeScheduleFromSchool["1PM"] = ['09','26','41','56']
timeScheduleFromSchool["2PM"] = ['13','30','47','56']
timeScheduleFromSchool["3PM"] = ['14','23','37','48','54']
timeScheduleFromSchool["4PM"] = ['05','21','27','37','48','58']
timeScheduleFromSchool["5PM"] = ['08','14','24','33','40','49']
timeScheduleFromSchool["6PM"] = ['01','16','32','56']
timeScheduleFromSchool["7PM"] = ['30','54']
timeScheduleFromSchool["8PM"] = ['22','41']
timeScheduleFromSchool["8PM"] = ['18']


# Concatenate a string of hours
def createStringOfHours(list) -> str:
    result = ""
    for item in list:
        temp = currentHour+":"+item+" "+ampm+"; "
        result += temp
    return result


# Checks if the user greeted the bot
def check_for_greeting(tokens) -> str:
    """If any of the words in the user's input was a greeting, return a greeting response"""
    for token in tokens:
        if token in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)


# Print a response based on the input
def find_next(station, number) -> str:
    currentSchedule = []
    if station == "diridon":
        currentSchedule = timeScheduleFromDiridon.get(currentHour+ampm)
    elif station == "school":
        currentSchedule = timeScheduleFromSchool.get(currentHour+ampm)
    if number == "1":
        for minute in currentSchedule:
            if currentMinute < minute:
                return currentHour+":"+minute+" "+ampm
    elif number == "2":
        index = 0
        for minute in currentSchedule:
            if currentMinute < minute:
                try:
                    return currentHour+":"+minute +" "+ampm+ " and " + currentHour+":"+currentSchedule[index+1]+" "+ampm
                except IndexError:
                    # This is an edge case. We are trying to return the next bus depart after the list ends
                    # Needs a better algorithm
                    return currentHour+":"+minute+" "+ampm
            index += 1


# Construct a response based on the user input
def construct_response(tokens) -> str:
    for token in tokens:
        if token in ACTIVATION_RESPONSES_DIRIDON:
            return createStringOfHours(timeScheduleFromDiridon.get(currentHour+ampm))
        elif token == "next":
            for token in tokens:
                if token == "2": # 2 is a string not int
                    for station in tokens:
                        if station == "diridon":
                            return find_next("diridon","2")
                        elif station == "school":
                            return find_next("school","2")
            for station in tokens:
                if station == "diridon":
                    return find_next("diridon", "1")
                elif station == "school":
                    return find_next("school", "1")


# Google Actions stuff
@app.route('/assistant',methods=['GET','POST'])
def g_assistant():

    # JSON parsing to get the query
    content = request.get_json()
    query5 = content['inputs'][0]['rawInputs'][0]['query']
    # query2 = query1[0]
    # query3 = query2['rawInputs']
    # query4 = query3[0]
    # query5 = query4['query']

    # NLP
    tokens = nltk.casual_tokenize(query5, preserve_case=False)  # Tokenize the input
    tokens.append(query5.lower())
    print("Tokens: " + str(tokens))

    greeting = check_for_greeting(tokens)   # Check for greeting
    response = construct_response(tokens)   # Check if there is a response

    if greeting:  # If the user greeted us
        print("Bot replies: " + greeting)
        return construct_json_response(greeting)
    if response:  # If the response was constructed
        print("Bot replied: Bus will depart at: " + response)
        return construct_json_response("Bus will depart at: " + response)
    elif greeting is None and response is None:
        print("Bot replied: I don't get that yet!")
        return construct_json_response("I don't get that yet!")


# Create a JSON constructor to respond to Google Assistant
def construct_json_response(message):
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


# For CLI
def print_response(sentence: str):
    tokens = nltk.casual_tokenize(sentence, preserve_case=False) # Tokenize the input

    greeting = check_for_greeting(tokens) # Check for greeting
    response = construct_response(tokens)

    if greeting: # If the user greeted us
        return greeting
    if response: # If the response was constructed
        return "Bus will depart at: " + response
    elif greeting is None and response is None:
        return "I don't get that yet! Type help to see what I can do :)"


# CLI
def main():

    return random.choice(GREETING_RESPONSES)
    while True:
        userInput = input("How can I help?\n")
        if userInput == 'quit' or userInput == 'exit':
            print("Closing Dash Bot!")
            break
        else:
            print_response(userInput)

# Run the program
# main()

# Run Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)