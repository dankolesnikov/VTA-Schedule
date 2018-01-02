# VTA ChatBot 
> Chat bot to assist VTA commuters

![](pics/logo.jpg)

## Conversational UI

Conversation I (bus schedule):

* User: Hello! 
* Bot: What bus or light rail schedule you'd like to know about?
* User: Dash bus from Diridon station
* Bot: Departures at 2:25 PM and 2:50 PM. Anything else I can help?

Conversation II (light rail schedule):

* User: Hello!
* Bot: What bus or light rail schedule you'd like to know about?
* User: Light rail from Fruitdale station
* Bot: What direction are you going?
* User: Winchester
* Bot: Departures at 2:40 PM and 2:50 PM. Anything else I can help?

Conversation III (hourly schedule)

Bus:

* User: Hello!
* Bot: What bus or light rail schedule you'd like to know about?
* User: Get schedule for Dash bus from Diridon station
* Bot: Departures for this hour are: 6:06 PM 6:22 PM 6:48 PM 6:22 PM 6:48 PM Anything else I can help?

Light rail:

* User: Hello!
* Bot: What bus or light rail schedule you'd like to know about?
* User: Get schedule for light rail from Diridon station towards winchester
* Bot: Departures for this hour are: 6:06 PM 6:22 PM 6:48 PM 6:22 PM 6:48 PM Anything else I can help?

## G Assistant Intents

Things you can ask in Google Assistant:

* Talk to VTA Schedule to get schedule for Dash bus from Diridon station
* Talk to VTA Schedule to get schedule for light rail from Diridon station towards winchester
* Talk to VTA Schedule to get next departures on light rail from Diridon station
* Talk to VTA Schedule to get next departures on Dash bus from Diridon station


## Supported VTA Routes

* Dash 201
* Light Rail 902 Mtn View <-> Winchester

To be added soon:

* Santa Teresa light rail
* Bus 181

### Directory 

    .
    ├── app.py                  # Contains logic, rules and CL UI
    ├── assistant.py            # Flask server for Google Assistant
    ├── data.py                 # Contains data for NLP
    ├── schedule.py             # Contains schedule for buses and light rail
    ├── state.py                # Helper class to maintain the state of the conversation
    ├── requirements.txt        # List of modules for Google App Engine
    ├── actions.json            # Google Actions file
    └── pics                    # Pictures
    
## Usage

Google Assistant:

Search G Assistant's app for 'VTA Schedule'

To run chat bot with Command Line UI:
```sh
python app.py
```
To run assistant locally on 8080 port:
```sh
python assistant.py
```
 
## Meta

Please feel free to reach out:)

Danil Kolesnikov – danil.kolesnikov@sjsu.edu

Distributed under the MIT license.
