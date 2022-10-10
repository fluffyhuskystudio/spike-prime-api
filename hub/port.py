from __future__ import annotations
from typing import Callable, Union, Optional, Iterable, Tuple, overload


class Pin():
    """
    This class can be used to read and control the two logic pins on pins 5 and 6 of each port. You can access two `Pin` objects via each `Port` instance if the port has been set to `MODE_GPIO` mode.
    
    Control a general purpose input/output (GPIO) pin.
    """

    def direction(self, direction: Optional[int]) -> int:
        """
        Gets and sets the direction of the pin.

        ### Parameters
        - `direction` - Choose 0 to make the pin an input or 1 to make it an output.

        ### Returns
        - The configured direction.
        """
        pass

    def value(self, value: Optional[int]) -> int:
        """
        Gets and sets the logic value of the pin.

        ### Parameters
        - `value` - Choose 1 to make the pin high or 0 to make it low. If the pin is configured as an input, this argument is ignored.

        ### Returns
        - Logic value of the pin.
        """
        pass

class Device():

    """
    This class is the blueprint for the device attributes of the ports in the `hub.port` module, which in turn are instances of the `Port` class. You cannot import or instantiate this class manually.
    
    Read values from a Powered Up device and configure its modes.
    """
    FORMAT_RAW = 0
    FORMAT_PCT= 1
    FORMAT_SI= 2

    def get(self, format: Optional[int]) -> list:
        """
        Gets the values that the active device mode provides.

        ### Parameters
        - `format` - Format of the data. Choose `FORMAT_RAW`, `FORMAT_PCT`, or `FORMAT_SI`.

        ### Returns
        - Values or measurements representing the device state.
        """
        pass

    @overload
    def mode(self, mode: int) -> None:
        pass

    @overload
    def mode(self, mode: int, data: bytes) -> None:
        pass

    @overload
    def mode(self, mode: Iterable[Tuple[int, int]]) -> None:
        pass

    @overload
    def mode(self) -> Iterable[Tuple[int, int]]:
        pass

    def pwm(self, value: int) -> None:
        pass

    def write_direct(self, data: bytes) -> None:
        pass

class Motor(Device):
    """
    This class is the blueprint for the motor attributes of the ports in the hub.port module, which in turn are instances of the Port class. You cannot import or instantiate this class manually.
    
    Control a motor.

    """
    BUSY_MODE = 0 #The port is busy configuring the device mode."""
    BUSY_MOTOR = 1 #The motor is busy executing a command.
    STOP_FLOAT = 0 #When stopping, the motor floats. See also float().
    STOP_BRAKE = 1 #When stopping, the motor brakes. See also brake().
    STOP_HOLD = 2 #When stopping, the motor holds position. See also hold().
    EVENT_COMPLETED = 0 #The motor command completed successfully.
    EVENT_INTERRUPTED = 1 #The motor command was interrupted.
    EVENT_STALLED = 2 #The motor command stopped because the motor was stalled.

    def __init__(self):
        pass

    def float(self) -> None:
        """
        Floats (coasts) the motor, as if disconnected from the hub.
        """
        pass

    def brake(self) -> None:
        """
        Passively brakes the motor, as if shorting the motor terminals.
        """
        pass

    def hold(self) -> None:
        """
        Actively hold the motor in its current position.
        """
        pass

    def busy(self, type:int = BUSY_MODE) -> bool:
        """
        Checks whether the motor is busy changing modes, or executing a motor command such as running to a position.

        ### Parameters
        - `type` - Choose `BUSY_MODE` or `BUSY_MOTOR`.

        ### Returns
        - Whether the motor is busy with the specified activity.
        """
        pass

    @overload
    def run_at_speed(self, speed: int) -> None:
        pass

    @overload
    def run_at_speed(self, speed: int, max_power: int, acceleration: int, deceleration: int, stall: bool) -> None:
        """
        Starts running a motor at the given speed.

        If a keyword argument is not given, its default value will be used.

        ### Parameters
        - `speed` - Sets the speed as a percentage of the rated speed for this motor. Positive means clockwise, negative means counterclockwise.

        ### Keyword Arguments
        - `max_power` - Sets percentage of maximum power used during this command.
        - `acceleration` - The time in milliseconds (0-10000) for the motor to reach maximum rated speed from standstill.
        - `deceleration` - The time in milliseconds (0-10000) for the motor to stop when starting from the maximum rated speed.
        - `stall` - Selects whether the motor should stop when stalled (True) or not (False).
        """
        pass

    @overload
    def run_for_time(self, msec: int) -> None:
        pass

    @overload
    def run_for_time(self, msec: int, speed: int, max_power: int, stop: int, acceleration: int, deceleration: int, stall: bool) -> None:
        """
        Runs a motor for a given amount of time.

        If a keyword argument is not given, its default value will be used.

        ### Parameters
        - `msec` - How long the motor should run in milliseconds. Negative values will be treated as zero.

        ### Keyword Arguments
        - `speed` - Sets the speed as a percentage of the rated speed for this motor. Positive means clockwise, negative means counterclockwise.
        - `max_power` - Sets percentage of maximum power used during this command.
        - `stop` - How to stop. Choose type: Choose `STOP_FLOAT`, `STOP_BRAKE`, or `STOP_HOLD`.
        - `acceleration` - The time in milliseconds (0-10000) for the motor to reach maximum rated speed from standstill.
        - `deceleration` - The time in milliseconds (0-10000) for the motor to stop when starting from the maximum rated speed.
        - `stall` - Selects whether the motor should stop trying to reach the endpoint when stalled (True) or not (False).
        """
        pass

    @overload
    def run_for_degrees(self, degrees: int) -> None:
        pass

    @overload
    def run_for_degrees(self, degrees: int, speed: int, max_power: int, stop: int, acceleration: int, deceleration: int, stall: bool) -> None:
        """
        Runs a motor for a given number of degrees at a given speed.

        If a keyword argument is not given, its default value will be used.

        ### Parameters
        - `degrees` - How many degrees to rotate relative to the starting point.

        ### Keyword Arguments
        - `speed` -

        Sets the speed as a percentage of the rated speed for this motor.

        If degrees > 0 and speed > 0, the motor turns clockwise.

        If degrees > 0 and speed < 0, the motor turns counterclockwise.

        If degrees < 0 and speed > 0, the motor turns clockwise.

        If degrees < 0 and speed < 0, the motor turns counterclockwise.

        - `max_power` - Sets percentage of maximum power used during this command.
        - `stop` - How to stop. Choose type: Choose `STOP_FLOAT`, `STOP_BRAKE`, or `STOP_HOLD`.
        - `acceleration` - The time in milliseconds (0-10000) for the motor to reach maximum rated speed from standstill.
        - `deceleration` - The time in milliseconds (0-10000) for the motor to stop when starting from the maximum rated speed.
        - `stall` - Selects whether the motor should stop trying to reach the endpoint when stalled (True) or not (False).
        """
        pass

    @overload
    def run_to_position(self, position: int) -> None:
        pass

    @overload
    def run_to_position(self, position: int, speed: int, max_power: int, stop: int, acceleration: int, deceleration: int, stall: bool) -> None:
        """
        Runs a motor to the given position.

        The angular position is measured relative to the motor position when the hub was turned on or when the motor was plugged in. You can preset this starting position using preset.

        If a keyword argument is not given, its default value will be used.

        ### Parameters
        - `position` - Position to rotate to.

        ### Keyword Arguments
        - `speed` - Sets the speed as a percentage of the rated speed for this motor. The sign of the speed will be ignored.
        - `max_power` - Sets percentage of maximum power used during this command.
        - `stop` - How to stop. Choose type: Choose STOP_FLOAT, STOP_BRAKE, or STOP_HOLD.
        - `acceleration` - The time in milliseconds (0-10000) for the motor to reach maximum rated speed from standstill.
        - `deceleration` - The time in milliseconds (0-10000) for the motor to stop when starting from the maximum rated speed.
        - `stall` - Selects whether the motor should stop trying to reach the endpoint when stalled (True) or not (False).
        """
        pass

    def preset(self, position: int) -> None:
        """
        Presets the starting position used by run_to_position.

        ### Parameters
        - `position` - The new position preset.
        """
        pass

    def callback(self, function: Callable[[int], None]) -> None:
        """
        Sets the callback function that is called when a command is completed, interrupted, or stalled.

        The function must accept one argument, which indicates why the callback was called. It will receive either EVENT_COMPLETED, EVENT_INTERRUPTED, or EVENT_STALLED.

        ### Parameters
        - `function` - Callable function that takes one argument. Choose None to disable the callback.
        """
        pass

    @overload
    def pid(self) -> tuple:
        pass

    @overload
    def pid(self, p: int, i: int, d: int) -> None:
        """
        Sets the p, i, and d constants of the motor PID controller.

        ### Parameters
        - `p` - Proportional constant.
        - `i` - Integral constant.
        - `d` - Derivative constant.

        ### Returns
        - If no arguments are given, this returns the values previously set by the user, if any. The system defaults cannot be read.
        """
        pass

    @overload
    def default(self) -> dict:
        pass
    
    @overload
    def default(self, speed: int, max_power: int, acceleration: int, deceleration: int, stop: int, pid: tuple, stall: bool, callback: Optional[Callable[[int], None]]):
        """
        Gets or sets the motor default settings. These are used by some of the methods listed above, when no explicit argument is given.

        ### Keyword Arguments
        - `speed` - The default speed.
        - `max_power` - The default max_power.
        - `acceleration` - The default acceleration.
        - `deceleration` - The default deceleration.
        - `stop` - The default stop argument.
        - `pid` - Tuple of p, i, and d. See also pid.
        - `stall` - The default stall argument.

        ### Returns
        - If no arguments are given, this returns the current settings.
        """
        pass

    def pair(self, other_motor: Motor) -> MotorPair:
        """
        Pairs this motor to other_motor to create a MotorPair object.

        You can only pair two different motors that are not already part of another pair. Both motors must be of the same type.

        ### Parameters
        - `other_motor` - The motor to pair to.

        ### Returns
        - On success, this returns the MotorPair object. It returns False to indicate an incompatible pair or None for other errors.
        """
        pass


class MotorPair():
    """
    This class can be used to control pairs of motors. You create `MotorPair` objects using the `pair()` method of a `Motor` object.
    
    Control two motors simultaneously in a synchronized way.
    """
    def __init__(self):
        pass

    def id(self) -> int:
        pass

    def primary(self) -> Motor:
        pass

    def secondary(self) -> Motor:
        pass

    def unpair(self) -> bool:
        pass

    def float(self) -> None:
        """
        Floats (coasts) the motor, as if disconnected from the hub.
        """
        pass

    def brake(self) -> None:
        """
        Passively brakes the motor, as if shorting the motor terminals.
        """
        pass

    def hold(self) -> None:
        """
        Actively hold the motor in its current position.
        """
        pass

    def pwm(self, pwm_0: int, pwm_1: int) -> None:
        pass
    
    @overload
    def run_at_speed(self, speed_0: int, speed_1: int) -> None:
        pass

    @overload
    def run_at_speed(self, speed_0: int, speed_1: int, max_power: int, acceleration: int, deceleration: int) -> None:
        pass

    @overload
    def run_for_time(self, msec: int) -> None:
        pass

    @overload
    def run_for_time(self, msec: int, speed_0: int, speed_1: int, max_power: int, acceleration: int, deceleration: int, stop: int) -> None:
        pass

    @overload
    def run_for_degrees(self, degrees: int) -> None:
        pass

    @overload
    def run_for_degrees(self, degrees: int, speed_0: int, speed_1: int, max_power: int, acceleration: int, deceleration: int, stop: int) -> None:
        pass

    @overload
    def run_to_position(self, position_0: int, position_1: int) -> None:
        pass

    @overload
    def run_to_position(self, position_0: int, position_1: int, speed: int, max_power: int, acceleration: int, deceleration: int, stop: int) -> None:
        pass

    def preset(self, position_0: int, position_1: int) -> None:
        pass

    def callback(self, function: Callable[[int], None]) -> None:
        pass

    def pid(self, p: int, i: int, d: int) -> None:
        pass

class Port():
    """
    This class is the blueprint for the port instances in the `hub.port` module. Those instances are automatically instantiated on boot, and further populated when devices are plugged in. You cannot import or instantiate this class manually.
    
    Provides access to port configuration and devices on a port. Some methods and attributes can only be used if the port is in the right mode, as shown below.

    Attributes for use with MODE_DEFAULT
    
    - `device`: Powered Up Device on this port. If no device is attached or the port is in a different mode, this attribute is None.
    - `motor`: Powered Up Motor on this port. If no motor is attached or the port is in a different mode, this attribute is None.
    """
    # motor: Motor
    # device: Device
    # p5: Pin
    # p6: Pin

    def __init__(self):
        self.motor: Motor
        self.device: Device
        self.p5: Pin
        self.p6: Pin

    def info(self) -> dict:
        pass

    def pwm(self, value: int) -> None:
        pass

    def callback(self, function: Callable[[int], None]) -> None:
        pass

    def mode(self, mode: int, baud_rate=2400) -> None:
        pass

    def baud(self, baud: int) -> None:
        pass

    def read(self, read: Union[int, any]) -> int:
        pass

    def write(self, write: bytes) -> int:
        pass


A: Port
B: Port
C: Port
D: Port
E: Port
F: Port

# Constants
## Port events
DETACHED = 0
ATTACHED = 1
## Port modes
MODE_DEFAULT = 0
MODE_FULL_DUPLEX = 1
MODE_HALF_DUPLEX = 2
MODE_GPIO = 3