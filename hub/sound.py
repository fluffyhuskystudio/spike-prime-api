from typing import Callable, overload

"""
The sound module lets you control the hub speaker to play sound files and beeps.
"""

@overload
def volume() -> int:
    pass

@overload
def volume(volume: int) -> None:
    """
    Sets the volume of the speaker.

    ### Parameters
    - volume - Volume between 0 (no sound) and 10 (maximum volume).

    ### Returns
    - If no argument is given, this returns the current volume.
    """
    pass

def beep(freq=1000, time=1000, waveform=0) -> None:
    """
    Starts beeping with a given frequency, duration, and wave form.

    ### Keyword Arguments
    - `freq` - Frequency of the beep in Hz (100 - 10000).
    - `time` - Duration of the beep in milliseconds (0 - 32767).
    - `waveform` - Wave form used for the beep. See constants for all possible values.
    """
    pass

def play(filename: str, rate=16000) -> None:
    """
    Starts playing a sound file.

    The sound file must be raw 16 bit data at 16 kHz.

    ### Parameters
    - `filename` - Absolute path to the sound file.

    ### Keyword Arguments
    - `rate` - Playback speed in Hz.

    ### Raises
    - `OSError (ENOENT)` - If the file does not exist.
    """
    pass

def callback(self, function: Callable[[int], None]) -> None:
    """
    Sets the callback function that is called when a sound finished playing or when it is interrupted.

    The function must accept one argument, whose value indicates why the callback was called:

    If the value is 0, the sound completed successfully.

    If the value is 1, the sound was interrupted.

    ### Parameters
    - `function` - Callable function that takes one argument. Choose None to disable the callback.
    """
    pass

#These values are used by the beep() function.
SOUND_SIN = 0 #The beep is a smooth sine wave.
SOUND_SQUARE = 1 #The beep is a loud and raw square wave.
SOUND_TRIANGLE = 2 #The beep has a triangular wave form.
SOUND_SAWTOOTH = 3 #The beep has a sawtooth-shaped wave form.

