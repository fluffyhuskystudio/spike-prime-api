from typing import Tuple, Callable
from typing import overload

def accelerometer(filtered=False) -> Tuple[int, int, int]:
    """
    Gets the acceleration of the hub along the x, y, and z axis.

    #### Parameters
    - `filtered` - Selecting True gives a more stable value, but it is delayed by 10-100 milliseconds. Selecting False gives the unfiltered value.

    #### Returns
    - Acceleration of the hub with units of `cm/s^2`. On a perfectly level surface, this gives (0, 0, 981).
    """
    pass

def gyroscope(filtered=False) -> Tuple[int, int, int]:
    """
    Gets the angular velocity of the hub along the x, y, and z axis.

    ### Parameters
    - `filtered` - Selecting True gives a more stable value, but it is delayed by 10-100 milliseconds. Selecting False gives the unfiltered value.

    ### Returns
    - Angular velocity with units of degrees per second.
    """
    pass

@overload
def align_to_model(top: int, front: int) -> None:
    pass

@overload
def align_to_model(nsamples: int, callback: Callable[[int], None]) -> None:
    pass

@overload
def align_to_model(top: int, front: int, nsamples: int, callback: Callable[[int], None]) -> None:
    """
    Sets the default hub orientation and/or calibrates the gyroscope.

    The hub must not move while calibrating. It takes about one second by default.

    Changing the model alignment affects most other methods in this module. They will now be relative to the hub alignment that you specify.

    ### Keyword Arguments
    - `top` - Which hub side is at the top of your model. See the hub `constants` for all possible values.
    - `front` - Which hub side is on the front of your model.
    - `nsamples` - Number of samples for calibration between 0 and 10000. It is 100 by default.
    - `callback` - Function that will be called when calibration is complete. It must accept one argument. Choose None to disable the callback. This is the default.
    """
    pass

@overload
def yaw_pitch_roll() -> Tuple[int, int, int]:
    pass

@overload
def yaw_pitch_roll(yaw_preset: int) -> None:
    pass

@overload
def yaw_pitch_roll(yaw_correction: float) -> None:
    """
    Gets the yaw, pitch, and roll angles of the hub, or resets the yaw.

    The yaw_correction is an optional keyword argument to improve the accuracy of the yaw value after one full turn. To use it:

    Reset the yaw angle to zero using def yaw_pitch_roll(0).

    Rotate the hub smoothly exactly one rotation clockwise.

    Call error = def yaw_pitch_roll()[0] to get the yaw error.

    The error should be 0. If it is not, you can set the correction using def yaw_pitch_roll(yaw_correction=error).

    For even more accuracy, you can turn clockwise 5 times, and use error / 5 as the correction factor.

    ### Keyword Arguments
    - `yaw_preset` - Sets the current yaw to the given value (-180 to 179).
    - `yaw_correction` - Adjusts the gain of the yaw axis values. See the yaw adjustment section below.

    ### Returns
    - If no arguments are given, this returns a tuple of yaw, pitch, and roll values in degrees.
    """
    pass

@overload
def orientation() -> int:
    pass

@overload
def orientation(callback: Callable[[int], None]) -> int:
    """
    Gets which hub side of the hub is mostly pointing up.

    ### Keyword Arguments
    - `callback` - Function that will be called when the orientation changes. It must accept one argument, which will tell you which hub side is up. Choose None to disable the callback. This is the default.
    
    ### Returns
    - Number representing which side is up. See hub constants for all possible values.
    """
    pass

@overload
def gesture() -> int:
    pass

@overload
def gesture(callback: Callable[[int], None]) -> int:
    """
    Gets the most recent gesture that the hub has made since this function was last called.

    ### Keyword Arguments
    - `callback` - Function that will be called when a gesture is detected. It must accept one argument, which will tell you which gesture was detected. Choose None to disable the callback. This is the default.

    ### Returns
    - Number representing the gesture. See motion constants for all possible values. If no gesture was detected since this function was last called, it returns None.
    """
    pass

#These values are used by the gesture() function.
TAPPED = 0 #The hub was tapped.
DOUBLETAPPED = 1 #The hub was quickly tapped twice.
SHAKE = 2 #The hub was shaken.
FREEFALL = 3 #The hub fell.