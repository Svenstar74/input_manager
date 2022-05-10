from Types import Types


class Input:

    def __init__(self, name, key, input_type=Types.KEYBOARD):
        """ Extension for keyboard keys to save their states keyup, keydown and pressed in a proper way.

        :param name: An identifier to simplify retrieving the key states by a custom set name
        :param key: The sdl2 key that should influence the input states (eg. sdl2.SDLK_q)
        """

        self.__name = name
        self.__key = key
        self.__type = input_type

        self.__keydown = False
        self.__keyup = False
        self.__pressed = False

    def update(self):
        self.__keydown = False
        self.__keyup = False

    def get_name(self):
        return self.__name

    def get_key(self):
        return self.__key

    def get_keydown(self):
        return self.__keydown

    def set_keydown(self, value):
        self.__keydown = value
        self.__pressed = value

    def get_keyup(self):
        return self.__keyup

    def set_keyup(self, value):
        self.__keyup = value
        self.__pressed = not value

    def get_pressed(self):
        return self.__pressed
