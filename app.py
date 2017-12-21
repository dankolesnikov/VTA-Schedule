import random
import nltk
import time
import data

# Setting up time data
current_time = time.strftime("%H:%M")
current_hour = time.strftime("%H")
current_minute = time.strftime("%M")
am_pm = time.strftime("%p")
isWeekend = False
print("Current time is: " + current_hour)

# Check is today is a weekend
if time.strftime("%w") is "0" or time.strftime("%w") == "6":
    isWeekend = True


# Concatenate a string of hours
def create_string_hours(minutes) -> str:
    """Helper method to create a string of departures from a list"""

    result = ''
    for minute in minutes:
        temp = format_ampm(minute) + '; '
        result += temp
    return "Schedule for the next hour is: " + result


def format_ampm(minute, hour = current_hour) -> str:
    """Convert 24 hour to 12 hour system"""

    t_24hour = hour + ":" + minute
    t = time.strptime(t_24hour, "%H:%M")
    timevalue_12hour = time.strftime("%I:%M %p", t)
    return timevalue_12hour


def find_next(station, number = "1") -> str:
    """Return 1 or 2 next departures from a particular station"""

    station_schedule_dict = dict([]) # set a local dictionary depending on the station
    if station == "diridon":
        station_schedule_dict = data.timeScheduleFromDiridon
    elif station == "school":
        station_schedule_dict = data.timeScheduleFromSchool

    current_schedule = station_schedule_dict.get(current_hour) # Set the local list with regard to current time

    if number == "1":
        for minute in current_schedule:
            if current_minute < minute:
                return 'Bus will depart at: ' + format_ampm(minute)
    elif number == "2":
        index = 0
        for minute in current_schedule:
            if current_minute < minute:
                try:
                    return 'Bus will depart at: ' + format_ampm(minute) + " and " + format_ampm(current_schedule[index + 1])
                except IndexError:  # Catch the case if the next departure is the last departure in the list
                        next_hour = str(int(current_hour) + 1)
                        next_hour_list = station_schedule_dict.get(next_hour)  # Get the list of the current schedule
                        next_minute = next_hour_list[0]
                        return 'Bus will depart at: ' + format_ampm(minute) + " and  " + format_ampm(next_minute,next_hour)
            index += 1


# Construct a response based on the user input
def construct_response(tokens) -> str:

    for token in tokens:
        if token in data.GREETING_KEYWORDS:  # If the user greeted us -> return a greeting
            return random.choice(data.GREETING_RESPONSES)

        if token in data.SCHEDULE_REQUESTS:  # User wants to see the schedule for the hour
            for station in tokens:
                if station == 'diridon':
                    return create_string_hours(data.timeScheduleFromDiridon.get(current_hour))
                elif station == 'school':
                    return create_string_hours(data.timeScheduleFromSchool.get(current_hour))

        elif token == "next":
            for number in tokens:
                if number == "2":    # 2 is a string not int
                    for station in tokens:
                        if station == 'diridon':
                            return find_next('diridon', '2')
                        elif station == "school":
                            return find_next('school', '2')

            # Return 1 departure time
            for station in tokens:
                if station == 'diridon':
                    return find_next("diridon")
                elif station == 'school':
                    return find_next("school")


def tokenize(sentence):
    """Takes a string and returns a list of tokens using NLTK"""

    tokens = nltk.casual_tokenize(sentence, preserve_case = False)  # Tokenize the input, all lowercase
    tokens.append(sentence.lower())
    print('Tokens: ' + str(tokens))
    return tokens


def respond(sentence):
    """Returns a response or a fail message"""
    tokens = tokenize(sentence)  # Tokenize the input
    response = construct_response(tokens)

    if response:  # If the response was constructed
        return response
    elif response is None: # No response
        return 'I dont know that yet :('


def main():
    """CL User Interface"""

    print(random.choice(data.GREETING_RESPONSES))
    while True:
        user_input = input('How can I help?\n')
        if user_input == 'quit' or user_input == 'exit':
            print('Closing..')
            break
        else:
            print(respond(user_input))


# Run the program
main()

