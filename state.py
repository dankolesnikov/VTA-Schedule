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
        if (self.mode == 'rail' or self.mode == 'light_rail') and self.station is not '' and self.direction is not '':
            self.state_rail = True
        else:
            self.state_rail = False
        return self.state_rail


    def get_state_dash(self):
        '''Method verifies if everything is ready to return departures from Dash bus'''
        if self.mode == 'dash' and self.station is not '':
            self.state_dash = True
        else:
            self.state_dash = False
        return self.state_dash


    def set_state(self, mode, station, direction = None):
        self.mode = mode
        self.station = station
        self.direction = direction
        print('State has been set!')


    def status(self):
        """Returns a status string with current mode, station, direction and readiness"""
        ready = False
        if self.mode == 'dash':
            ready = self.get_state_dash()
        elif self.mode == 'rail' or 'light_rail':
            ready = self.get_state_rail()
        return f'Context status:  Mode: {self.mode} Station: {self.station} Direction: {self.direction} Ready: {ready}'


    def reset(self):
        """Resets the state of the context"""
        self.state_rail = False
        self.state_dash = False
        self.mode = ''
        self.station = ''
        self.direction = ''



