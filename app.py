import nltk
import time
import logging
import data
import schedule
import pytz
from pytz import timezone
from datetime import datetime
from state import State

# Initialize vars
current_time = ''
current_hour = ''
current_minute = ''
temp_mode = ''
temp_station = ''
temp_direction = ''
context = State(temp_mode, temp_station, temp_direction) # Setup state


# Setting up time data from UTC to PST
def set_time():
    """Set up global time variables"""
    utc_dt = pytz.utc.localize(datetime.utcnow())
    pst_tz = timezone('US/Pacific')
    pst_dt = pst_tz.normalize(utc_dt.astimezone(pst_tz))
    format = '%H%M'
    global current_time
    current_time = pst_dt.strftime(format)
    current_time = '1820'
    global current_hour
    current_hour = pst_dt.strftime("%H")
    current_hour = '18'
    global current_minute
    current_minute = pst_dt.strftime("%M")
    current_minute = '20'

# Logger setup
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
handler = logging.FileHandler('logs.log')
handler.setLevel(logging.INFO)
log.addHandler(handler)


# Print current time
set_time()
time_data = f'Current time: {current_time}\nCurrent hour: {current_hour}\nCurrent minute: {current_minute}'
log.info("Time data: %s", time_data)
isWeekend = False

# Check is today is a weekend
if time.strftime("%w") is "0" or time.strftime("%w") == "6":
    isWeekend = True


def create_string_hours(minutes) -> str:
    """Helper method to create a string of departures from a list"""
    result = ''
    for minute in minutes:
        temp = format_ampm(minute) + ', '
        result += temp
    return "Schedule for the this hour is: " + result


def format_ampm(time_24hour) -> str:
    """Convert 24 hour to 12 hour system"""
    t = time.strptime(time_24hour, "%H%M")  # Create time object
    timevalue_12hour = time.strftime("%-I:%M %p", t)  # e.g. From 08:14 to 8:14 AM or 15:24 to 3:24 PM
    return timevalue_12hour


def find_next(mode, station, direction, number = "1") -> str:
    """Return 1 or 2 next departures from a particular station
        Create new recursive algorithm"""
    station_schedule_dict = dict([])  # set a local dictionary depending on the station

    if mode == 'dash':
        station_schedule_dict = schedule.timeSchedule.get('dash').get(station)
    elif mode == 'rail' or mode == 'light_rail':
        station_schedule_dict = schedule.timeSchedule.get('rail').get(direction).get(station)

    next_hour = str(int(current_hour) + 1)  # Next hour
    next_hour_struct = time.strptime(next_hour, "%H")
    next_hour_object = time.strftime("%H", next_hour_struct)

    try:
        current_schedule = station_schedule_dict.get(current_hour) + station_schedule_dict.get(next_hour_object)  # Concatenate the schedule of the current hour with the scheule of the next hour
    except (IndexError, TypeError):
        return "No departures!"

    if number == '1': # Return 1 departure
        for departure in current_schedule:
            if current_time < departure:
                return 'Departure from '+ station +' station at: ' + format_ampm(departure)

    if number == '2': # Return 2 departures
        index = 0 # Keep track of the current position in the array
        for departure in current_schedule:
            if current_time < departure:
                try:
                    next_departure = current_schedule[index + 1]
                    return 'Departure from ' + station + ' station at: ' + format_ampm(departure) + " and " + format_ampm(next_departure)
                except (IndexError, TypeError):
                    return "No departures!"
            index += 1


def construct_response(tokens) -> str:
    """ Construct and return a response based on tokenizes user input"""
    set_time()  # update time
    global temp_mode
    global temp_direction
    global temp_station
    global context

    for token in tokens:
        if token in data.GREETING_KEYWORDS:  # If the user greeted us -> return a greeting
            return 'What bus or light rail schedule you like to know about?'
        if token in data.SCHEDULE_REQUESTS:  # User wants to see the schedule for current hour for specific station
            for station in tokens:
                if station in data.STATIONS_LIST:
                    for mode in tokens:
                        if mode in data.MODE_LIST:
                            if mode == 'dash':
                                return create_string_hours(schedule.timeSchedule.get('dash').get(station).get(current_hour))
                            elif mode == 'rail' or 'light_rail':
                                for direction in tokens:
                                    if direction in data.DIRECTION_LIST:
                                        return create_string_hours(schedule.timeSchedule.get('rail').get(direction).get(station).get(current_hour))

        elif token in data.MODE_LIST:  # Mode of transportation and station were entered
            temp_mode = token
            context.mode = token  # Set the context
            for station in tokens:
                if station in data.STATIONS_LIST:
                    temp_station = station
                    context.station = station  # Add to the context
                    if context.get_state_dash():  # Check if all variable are ready for dash bus
                        log.info("Dash's state: %s", context.is_ready('dash'))
                        context.reset()
                        return find_next(temp_mode,temp_station,temp_direction, '2')
                    else:
                        return 'What direction are you going?'  # This must be a rail conversation
            return 'What station are you going?'

        elif token in data.DIRECTION_LIST:  # Check is user indicated direction of travel
            temp_direction = token
            context.direction = token
            if context.get_state_rail():  # Check if we all vars are ready for rail departure
                log.info("Rail's state: %s", context.is_ready('rail'))
                context.reset()
                return find_next(temp_mode, temp_station, temp_direction, '2')  # Return next 2 departures
            else:
                log.info('Error in the end', context.is_ready('rail'))
                return 'Opps! Something went wrong. Try again!'


def tokenize(sentence):
    """Takes a string and returns a list of tokens using NLTK"""
    tokens = nltk.casual_tokenize(sentence, preserve_case = False)  # Tokenize the input, all lowercase
    list = post_process(tokens)
    list.append(sentence)
    log.info("Tokens: %s", list)
    return list

def post_process(tokens):
    '''Performs Named Entity Recognition on the set of tokens to find station and directions that contain 2 words.
    \post_process will concatenate with the following word using underscore'''
    index = 0
    result = list([])
    for word in tokens:
        if word in data.NER_KEYWORDS: # if the word is part of the entities list
            result.append(word + '_' + tokens[index+1])
        else:
            result.append(word)
        index += 1
    return result


def respond(sentence):
    """Returns a response or a fail message"""
    set_time()
    tokens = tokenize(sentence)  # Tokenize the input
    response = construct_response(tokens)

    if response:  # If the response was constructed
        log.info("Response was returned: %s", response)
        return response
    elif response is None: # No response
        log.debug('Failed to respond. Tokens: $s', tokens)
        return None


print('What bus or light rail schedule youd like to know about?')
def main():
    """CL User Interface"""
    user_input = input()
    response = respond(user_input)

    if response is not None:
        print(f'Response: {response}')
        main()
    elif user_input == 'engage':
        print('What bus or light rail schedule youd like to know about?')
        main()
    else:
        log.debug('Error %s', response)
        main()


# Run CL UI, disable when deploying
#main()



