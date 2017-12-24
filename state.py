class State:
    '''Helper class to maintain the state of application'''
    def __init__(self, mode, station, direction):
        '''State can be: ready or not ready'''
        self.state_rail = False
        self.state_dash = False
        self.mode = mode
        self.station = station
        self.direction = direction


    def get_state_rail(self):
        '''Method verifies if everything is ready to return departures from rail'''
        if self.mode == 'rail' or self.mode == 'light_rail' and self.station is not None and self.direction is not None:
            self.state_rail = True
            return self.state_rail


    def get_state_dash(self):
        '''Method verifies if everything is ready to return departures from Dash bus'''
        if self.mode == 'dash' and self.station is not None:
            self.state_dash = True
            return self.state_dash


    def set_state(self, mode, station, direction = None):
        self.mode = mode
        self.station = station
        self.direction = direction
        print('State has been set!')

    def is_ready(self, mode):
        if mode == 'rail' or mode == 'light_rail' and self.get_state_rail() is True:
            return 'Rail is ready!'
        elif mode == 'rail' or mode == 'light_rail' and self.get_state_rail() is False:
            return 'Rail isnt ready!'
        if mode == 'dash' and self.get_state_dash() is True:
            return 'Dash is ready!'
        elif mode == 'dash' and self.get_state_dash() is False:
            return 'Dash isnt ready!'

    def reset(self):
        """Resets the state of the context"""
        self.state_rail = False
        self.state_dash = False
        self.mode = ''
        self.station = ''
        self.direction = ''



