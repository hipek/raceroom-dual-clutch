import gremlin
from gremlin.user_script import *

# ======= USER SETTINGS =======
mode = ModeVariable("Mode", "Mode in which to use these settings", True)

invert_axis = BoolVariable(
    "Invert Pedal",
    "Reverse the clutch pedal axis",
    False
)

clutch_pedal = PhysicalInputVariable(
    "Clutch Pedal Axis",
    "Your real clutch pedal axis",
    valid_types=[gremlin.common.InputType.JoystickAxis],
    is_optional=False,
)

clutch_button = PhysicalInputVariable(
    "Dual Clutch Button",
    "Button that activates 100% clutch",
    valid_types=[gremlin.common.InputType.JoystickButton],
    is_optional=False,
)

clutch_output = VirtualInputVariable(
    "vJoy Clutch Axis",
    "Output vJoy axis",
    valid_types=[gremlin.common.InputType.JoystickAxis],
    is_optional=False,
)

# ======= INTERNAL STATE =======
force_override = False
last_pedal_value = 0.0

# Decorators
pedal_dec = clutch_pedal.create_decorator(mode.value)
button_dec = clutch_button.create_decorator(mode.value)


# ======= PEDAL HANDLER =======
@pedal_dec.axis(clutch_pedal.input_id)
def pedal_cb(event, vjoy):
    global last_pedal_value, force_override

    if invert_axis.value:
        last_pedal_value = -event.value
    else:
        last_pedal_value = event.value

    if not force_override:
        vjoy[clutch_output.vjoy_id].axis(clutch_output.input_id).value = last_pedal_value


# ======= BUTTON HANDLER =======
@button_dec.button(clutch_button.input_id)
def button_cb(event, vjoy):
    global force_override, last_pedal_value

    axis = vjoy[clutch_output.vjoy_id].axis(clutch_output.input_id)

    if event.is_pressed:
        # Activate forced 100% clutch
        force_override = True
        axis.value = 1.0
    else:
        # Return control to pedal
        force_override = False
        axis.value = last_pedal_value
