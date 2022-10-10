from typing import Callable


class Button:
    """
    Provides access to button state and callback.

    Each of the buttons listed below are instances of this class. You cannot instantiate additional button objects.
    """

    def is_pressed(self) -> bool:
        """
        Gets the state of the button.

        ### Returns
        - True if it is pressed, False otherwise.
        """
        pass

    def was_pressed() -> bool:
        """
        Checks if this button was pressed since this method was last called.

        ### Returns
        - True if it was pressed at least once since the previous call, False otherwise.
        """
        pass

    def presses() -> int:
        """
        Gets the number of times this button was pressed since this method was last called.

        ### Returns
        - The number of presses since the last call.
        """
        pass

    def callback(function: Callable[[int], None]) -> None:
        """
        Sets the callback function that is called when the button is pressed and when it is released.

        The function must accept one argument, whose value indicates why the callback was called:

        If the value is 0, the button is now pressed.

        Otherwise, the button is now released. The value represents how many milliseconds it was pressed before it was released.

        ### Parameters
        - `function` - Callable function that takes one argument. Choose None to disable the callback.
        """
        pass


left: Button  # The left button.
right: Button  # The right button.
center: Button  # The center button.
connect: Button  # The button with the Bluetooth symbol.