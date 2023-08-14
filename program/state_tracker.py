
class drone_state:
    def __init__(self, start_position):
        self.start = start_position
    # position during flight and height could be calculated by tracking the changes in respect to the starting position
    # It would be pretty straight forward (no obstacles in flight field) but when we want to allow the cmd "rotate"
    # thing starting to get complicated (geometry is needed)