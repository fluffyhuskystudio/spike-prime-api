from typing import Callable

"""
The supervision module lets you monitor critical states of the hub.
"""

def info() -> dict:
    """
    Gets status information from the subsystem that supervises the hub.

    This returns a dictionary of the form:

    ```
    {
        # Checks if the peak current is too high.
        'peek_current_too_high': False,

        # Checks if the current is too high.
        'continous_current_too_high': False,

        # The current value in mA.
        'continuous_current': 60,

        # Checks if the hub temperature is too high.
        'temperature_too_high': False
    }
    ```
    ### Returns
    - Supervision status information.
    """
    pass

def callback(self, function: Callable[[int], None]) -> None:
    """
    Sets the callback function that is called when an over-current event occurs.

    The function must accept one argument, which indicates the current in mA that triggered the callback.

    ### Parameters
    - `function` - Callable function that takes one argument. Choose None to disable the callback.
    """
    pass