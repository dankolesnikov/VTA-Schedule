

# Dictionaries contain schedule(24 hour) for a particular station

# From Diridon Station
timeScheduleFromDiridonDash = dict([])
timeScheduleFromDiridonDash['06'] = ['0634', '0651']
timeScheduleFromDiridonDash['07'] = ['0706', '0714', '0723', '0730', '0740', '0748', '0752']
timeScheduleFromDiridonDash['08'] = ['0803', '0809', '0816', '0824', '0835', '0840', '0847', '0850']
timeScheduleFromDiridonDash['09'] = ['0909', '0916', '0924', '0940', '0947']
timeScheduleFromDiridonDash['10'] = ['1002', '1016', '1030', '1045']
timeScheduleFromDiridonDash['11'] = ['1101', '117', '131', '145']
timeScheduleFromDiridonDash['12'] = ['1200', '1215', '1230', '1245']
timeScheduleFromDiridonDash['13'] = ['1302', '1319', '1334', '1349']
timeScheduleFromDiridonDash['14'] = ['1406', '1423', '1440', '1449']
timeScheduleFromDiridonDash['15'] = ['1507', '1516', '1529', '1540', '1546', '1556']
timeScheduleFromDiridonDash['16'] = ['1606', '1612', '1618', '1628', '1638', '1648', '1658']
timeScheduleFromDiridonDash['17'] = ['1704', '1714', '1723', '1730', '1739', '1751']
timeScheduleFromDiridonDash['18'] = ['1806', '1822', '1848', '1822', '1848']
timeScheduleFromDiridonDash['19'] = ['1922', '1947']
timeScheduleFromDiridonDash['20'] = ['2015', '2034']
timeScheduleFromDiridonDash['21'] = ['2111']
timeScheduleFromDiridonDash['22'] = ['2200']

# From SJSU Campus
timeScheduleFromSchoolDash = dict([])
timeScheduleFromSchoolDash['06'] = ['0641', '0658']
timeScheduleFromSchoolDash['07'] = ['0713', '0721', '0738', '0748', '0756']
timeScheduleFromSchoolDash['08'] = ['0800', '0811', '0817', '0824', '0832', '0843', '0848', '0855']
timeScheduleFromSchoolDash['09'] = ['0904', '0917', '0924', '0932', '0947', '0954']
timeScheduleFromSchoolDash['10'] = ['1009', '1023', '1037', '1052']
timeScheduleFromSchoolDash['11'] = ['1108', '1124', '1138', '1152']
timeScheduleFromSchoolDash['12'] = ['1207', '1222', '1237', '1252']
timeScheduleFromSchoolDash['13'] = ['1309', '1326', '1341', '1356']
timeScheduleFromSchoolDash['14'] = ['1413', '1430', '1447', '1456']
timeScheduleFromSchoolDash['15'] = ['1514', '1523', '1537', '1548', '1554']
timeScheduleFromSchoolDash['16'] = ['1605', '1621', '1627', '1637', '1648', '1658']
timeScheduleFromSchoolDash['17'] = ['1708', '1714', '1724', '1733', '1740', '1749']
timeScheduleFromSchoolDash['18'] = ['1801', '1816', '1832', '1856']
timeScheduleFromSchoolDash['19'] = ['1930', '1954']
timeScheduleFromSchoolDash['20'] = ['2022', '2041']
timeScheduleFromSchoolDash['21'] = ['2118']
timeScheduleFromSchoolDash['22'] = ['2200']


# Dict of dicts
timeScheduleDash = dict([])
timeScheduleDash['diridon'] = timeScheduleFromDiridonDash
timeScheduleDash['school'] = timeScheduleFromSchoolDash


# Rail Schedule going towards winchester from fruitdale station
timeScheduleRailWinchesterFruitdale = dict([])
timeScheduleRailWinchesterFruitdale['18'] = ['1809', '1823', '1837', '1852']
timeScheduleRailWinchesterFruitdale['19'] = ['1909', '1923', '1952', '1957']


# Rail Schedule going towards winchester from diridon station
timeScheduleRailWinchesterDiridon = dict([])
timeScheduleRailWinchesterDiridon['18'] = ['1809', '1823', '1857', '1858']
timeScheduleRailWinchesterDiridon['19'] = ['1909', '1923', '1947', '1952']



# timeScheduleRailWinchester has light rail schedule for a train leaving towards Winchester based on a station
timeScheduleRailWinchester = dict([])
timeScheduleRailWinchester['fruitdale'] = timeScheduleRailWinchesterFruitdale
timeScheduleRailWinchester['diridon'] = timeScheduleRailWinchesterDiridon

# timeScheduleRailMtnView has light rail schedule for a train leaving towards Mtn View based on a station
timeScheduleRailMtnView = dict([])
timeScheduleRailMtnView['diridon'] = []

# timeScheduleRailDirection contains schedules for light rail based on direction
timeScheduleRailDirection = dict([])
timeScheduleRailDirection['winchester'] = timeScheduleRailWinchester
timeScheduleRailDirection['downtown'] = timeScheduleRailMtnView
timeScheduleRailDirection['alum'] = []
timeScheduleRailDirection['santa_teresa'] = timeScheduleRailWinchester

# timeSchedule contains the dictionaries of 2
timeSchedule = dict([])
timeSchedule['rail'] = timeScheduleRailDirection
timeSchedule['dash'] = timeScheduleDash




