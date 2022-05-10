class Axis:

    def __init__(self, name, negative_button, positive_button, gravity, dead, sensitivity, snap):
        """ An axis simplifies some kinds of movements by handling two input buttons simultaneously.
        The value of the axis will always stay between -1 and 1 to define the current state of the axis.

        :param name: An identifier to access the axis, eg. 'horizontal'
        :param negative_button: An Input that decreases the axis' value
        :param positive_button: An Input that increases the axis' value
        :param gravity: Speed that the axis falls toward neutral when no input is present
        :param dead: The dead zone around zero, where the value will count as exactly zero
        :param sensitivity: Speed that the axis will move towards the target value
        :param snap: If enabled, the axis value will reset to zero when going in the opposite direction
        """

        self.__name = name
        self.__negative_button = negative_button
        self.__positive_button = positive_button

        self.__gravity = gravity
        self.__dead = dead
        self.__sensitivity = sensitivity
        self.__snap = snap

        self.__value = 0

    def update(self):

        # Let the button return to zero
        if self.__value > 0:
            self.__value -= self.__gravity
        elif self.__value < 0:
            self.__value += self.__gravity

        # Reset the value if snap takes action
        if self.__positive_button.get_pressed() and self.__value < 0 and self.__snap:
            self.__value = 0

        if self.__negative_button.get_pressed() and self.__value > 0 and self.__snap:
            self.__value = 0

        # Update the value of the axis based on the input buttons
        if self.__positive_button.get_pressed():
            self.__value += self.__sensitivity
        if self.__negative_button.get_pressed():
            self.__value -= self.__sensitivity

        # Limit the value to a range of -1 to 1
        if self.__value > 1.0:
            self.__value = 1.0
        if self.__value < -1.0:
            self.__value = -1.0

    def get_value(self):
        if - self.__dead < self.__value < self.__dead:
            return 0
        else:
            return self.__value

    def get_name(self):
        return self.__name
