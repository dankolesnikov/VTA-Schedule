# Keywords for NLP later

# User greeted the bot with any of these
GREETING_KEYWORDS = [
    "hello", "hi", "greetings",
    "hey", "whats up",
    "talk to vta bot"]

# Reply with these words if the user greeted us
GREETING_RESPONSES = ["Hey commuter!", "Hello commuter!"]

# Keywords when the user requested a schedule for current hour
SCHEDULE_REQUESTS = ["schedule",
                     "get schedule",
                     'talk to vta bot to get schedule']

# List of available station; station with 2 words must be separate by underscore _
STATIONS_LIST = ['diridon',
                 'santa_clara',
                 'convention_center',
                 'fruitdale',
                 'school']

# Named Entity Recognition list for stations and directions with 2 words
NER_KEYWORDS = ['santa',
                'convention',
                'alum',
                'light']

# List of possible directions
DIRECTION_LIST = ['winchester',
                  'downtown',
                  'mountain view',
                  'santa_teresa',
                  'alum_rock']

# List of transport modes
MODE_LIST = ['dash', 'rail', 'light_rail']


