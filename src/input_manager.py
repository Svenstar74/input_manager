import sdl2
import sdl2.ext
import ctypes
import sys

from Input import Input
from Axis import Axis
from Types import Types


def update():

    global __inputs, __axes, __mouse_x, __mouse_y, __rel_mouse_x, __rel_mouse_y

    # Reset values for all inputs
    for i in __inputs:
        i.update()

    __rel_mouse_x = 0
    __rel_mouse_y = 0

    # Look for changes in inputs and update their states
    for event in sdl2.ext.get_events():

        if event.type == sdl2.SDL_QUIT:
            sys.exit()

        # https://stackoverflow.com/questions/59725849/sdl-keyup-triggered-when-key-is-still-down
        # Top answer explains this
        if event.key.repeat != 0:
            continue

        if event.type == sdl2.SDL_KEYDOWN:
            input_instance = get_input_by_key(event.key.keysym.sym)
            if input_instance:
                input_instance.set_keydown(True)

        if event.type == sdl2.SDL_KEYUP:
            input_instance = get_input_by_key(event.key.keysym.sym)
            if input_instance:
                input_instance.set_keyup(True)

        if event.type == sdl2.SDL_MOUSEMOTION:
            __mouse_x = event.motion.x
            __mouse_y = event.motion.y
            __rel_mouse_x = event.motion.xrel
            __rel_mouse_y = event.motion.yrel

        if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
            input_instance = get_input_by_key(event.button.button)
            if input_instance:
                input_instance.set_keydown(True)

        if event.type == sdl2.SDL_MOUSEBUTTONUP:
            input_instance = get_input_by_key(event.button.button)
            if input_instance:
                input_instance.set_keyup(True)

    # After all inputs are up-to-date, update every axis as well
    for a in __axes:
        a.update()


def get_input_by_name(name):

    global __inputs

    for i in __inputs:
        if name.lower() == i.get_name():
            return i
    return False


def get_input_by_key(key):

    global __inputs

    for i in __inputs:
        if key == i.get_key():
            return i
    return False


def get_axis(name):

    global __axes

    for a in self.__axes:
        if name == a.get_name():
            return a
    return False


def get_mouse_pos():
    return __mouse_x, __mouse_y


def get_mouse_movement():
    return __rel_mouse_x, __rel_mouse_y


sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

# region Inputs that are not yet Implemented
# K_0
# K_1
# K_2
# K_3
# K_4
# K_5
# K_6
# K_7
# K_8
# K_9
#
# K_AC_BACK
# K_AMPERSAND
# K_ASTERISK
# K_AT
# K_BACKQUOTE
# K_BACKSLASH
# K_BACKSPACE
# K_BREAK
# K_CAPSLOCK
# K_CARET
# K_CLEAR
# K_COLON
# K_COMMA
# K_CURRENCYSUBUNIT
# K_CURRENCYUNIT
# K_DELETE
# K_DOLLAR
# K_DOWN
# K_END
# K_EQUALS
#
# K_EURO
# K_EXCLAIM
# K_F1
# K_F10
# K_F11
# K_F12
# K_F13
# K_F14
# K_F15
# K_F2
# K_F3
# K_F4
# K_F5
# K_F6
# K_F7
# K_F8
# K_F9
# K_GREATER
# K_HASH
# K_HELP
# K_HOME
# K_INSERT
# K_KP0
# K_KP1
# K_KP2
# K_KP3
# K_KP4
# K_KP5
# K_KP6
# K_KP7
# K_KP8
# K_KP9
# K_KP_0
# K_KP_1
# K_KP_2
# K_KP_3
# K_KP_4
# K_KP_5
# K_KP_6
# K_KP_7
# K_KP_8
# K_KP_9
# K_KP_DIVIDE
# K_KP_ENTER
# K_KP_EQUALS
# K_KP_MINUS
# K_KP_MULTIPLY
# K_KP_PERIOD
# K_KP_PLUS
# K_LALT
# K_LCTRL
# K_LEFT
# K_LEFTBRACKET
# K_LEFTPAREN
# K_LESS
# K_LGUI
# K_LMETA
# K_LSUPER
# K_MENU
# K_MINUS
# K_MODE
# K_NUMLOCK
# K_NUMLOCKCLEAR
# K_PAGEDOWN
# K_PAGEUP
# K_PAUSE
# K_PERCENT
# K_PERIOD
# K_PLUS
# K_POWER
# K_PRINT
# K_PRINTSCREEN
# K_QUESTION
# K_QUOTE
# K_QUOTEDBL
# K_RALT
# K_RCTRL
# K_RETURN
# K_RGUI
# K_RIGHT
# K_RIGHTBRACKET
# K_RIGHTPAREN
# K_RMETA
# K_RSHIFT
# K_RSUPER
# K_SCROLLLOCK
# K_SCROLLOCK
# K_SEMICOLON
# K_SLASH
# K_SYSREQ
# K_TAB
# K_UNDERSCORE
# K_UNKNOWN
# K_UP
# endregion
__inputs = [
    Input('a', sdl2.SDLK_a),
    Input('b', sdl2.SDLK_b),
    Input('c', sdl2.SDLK_c),
    Input('d', sdl2.SDLK_d),
    Input('e', sdl2.SDLK_e),
    Input('f', sdl2.SDLK_f),
    Input('g', sdl2.SDLK_g),
    Input('h', sdl2.SDLK_h),
    Input('i', sdl2.SDLK_i),
    Input('j', sdl2.SDLK_j),
    Input('k', sdl2.SDLK_k),
    Input('l', sdl2.SDLK_l),
    Input('m', sdl2.SDLK_m),
    Input('n', sdl2.SDLK_n),
    Input('o', sdl2.SDLK_o),
    Input('p', sdl2.SDLK_p),
    Input('q', sdl2.SDLK_q),
    Input('r', sdl2.SDLK_r),
    Input('s', sdl2.SDLK_s),
    Input('t', sdl2.SDLK_t),
    Input('u', sdl2.SDLK_u),
    Input('v', sdl2.SDLK_v),
    Input('w', sdl2.SDLK_w),
    Input('x', sdl2.SDLK_x),
    Input('y', sdl2.SDLK_y),
    Input('z', sdl2.SDLK_z),

    Input('escape', sdl2.SDLK_ESCAPE),

    Input('space', sdl2.SDLK_SPACE),
    Input('lshift', sdl2.SDLK_LSHIFT),

    Input('lmb', sdl2.SDL_BUTTON_LEFT, Types.MOUSE),
    Input('rmb', sdl2.SDL_BUTTON_RIGHT, Types.MOUSE),
    Input('mousewheel', sdl2.SDL_BUTTON_MIDDLE, Types.MOUSE)
]

__axes = [Axis('horizontal', get_input_by_name('a'), get_input_by_name('d'), 0.2, 0.3, 1.5, True),
          Axis('vertical', get_input_by_name('w'), get_input_by_name('s'), 0.2, 0.3, 1.5, True)]

__mouse_x = 0
__mouse_y = 0

__rel_mouse_x = 0
__rel_mouse_y = 0
