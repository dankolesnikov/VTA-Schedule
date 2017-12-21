



# Keywords for NLP later
GREETING_KEYWORDS = [
    "hello", "hi", "greetings",
    "hey", "whats up",
    "talk to dash bus"]

GREETING_RESPONSES = ["Hey commuter!", "Hello commuter!"]

SCHEDULE_REQUESTS = ["schedule",
                     "get schedule",
                     'talk to dash bus to get schedule']


# Dictionaries contain schedule(24 hour) for a particular station

# From Diridon Station
timeScheduleFromDiridon = dict([])
timeScheduleFromDiridon['06'] = ['34', '51']
timeScheduleFromDiridon['07'] = ['06', '14', '23', '30', '40', '48', '52']
timeScheduleFromDiridon['08'] = ['03', '09', '16', '24', '35', '40', '47', '50']
timeScheduleFromDiridon['09'] = ['09', '16', '24', '40', '47']
timeScheduleFromDiridon['10'] = ['02', '16', '30', '45']
timeScheduleFromDiridon['11'] = ['01', '17', '31', '45']
timeScheduleFromDiridon['12'] = ['00', '15', '30', '45']
timeScheduleFromDiridon['13'] = ['02', '19', '34', '49']
timeScheduleFromDiridon['14'] = ['06', '23', '40', '49']
timeScheduleFromDiridon['15'] = ['07', '16', '29', '40', '46', '56']
timeScheduleFromDiridon['16'] = ['06', '12', '18', '28', '38', '48', '58']
timeScheduleFromDiridon['17'] = ['04', '14', '23', '30', '39', '51']
timeScheduleFromDiridon['18'] = ['06', '22', '48', '22', '48']
timeScheduleFromDiridon['19'] = ['22', '47']
timeScheduleFromDiridon['20'] = ['15', '34']
timeScheduleFromDiridon['21'] = ['11']
timeScheduleFromDiridon['22'] = ['00']

# From SJSU Campus
timeScheduleFromSchool = dict([])
timeScheduleFromSchool['06'] = ['41', '58']
timeScheduleFromSchool['07'] = ['13', '21', '38', '48', '56']
timeScheduleFromSchool['08'] = ['00', '11', '17', '24', '32', '43', '48', '55']
timeScheduleFromSchool['09'] = ['04', '17', '24', '32', '47', '54']
timeScheduleFromSchool['10'] = ['09', '23', '37', '52']
timeScheduleFromSchool['11'] = ['08', '24', '38', '52']
timeScheduleFromSchool['12'] = ['07', '22', '37', '52']
timeScheduleFromSchool['13'] = ['09', '26', '41', '56']
timeScheduleFromSchool['14'] = ['13', '30', '47', '56']
timeScheduleFromSchool['15'] = ['14', '23', '37', '48', '54']
timeScheduleFromSchool['16'] = ['05', '21', '27', '37', '48', '58']
timeScheduleFromSchool['17'] = ['08', '14', '24', '33', '40', '49']
timeScheduleFromSchool['18'] = ['01', '16', '32', '56']
timeScheduleFromSchool['19'] = ['30', '54']
timeScheduleFromSchool['20'] = ['22', '41']
timeScheduleFromSchool['21'] = ['18']
timeScheduleFromSchool['22'] = ['00']
