from typing import Union

def voltage() -> int:
    """
    Gets the battery voltage.

    ### Returns
    - The voltage in mV.
    """
    pass

def current() -> int:
    """
    Gets current flowing out of the battery.

    ### Returns
    - The current in in mA.
    """
    pass

def capacity_left() -> int:
    """
    Gets the remaining capacity as a percentage of a fully charged battery.

    ### Returns
    - The remaining battery capacity.
    """
    pass

def temperature() -> float:
    """
    Gets the temperature of the battery.

    ### Returns
    - The temperature in degrees Celsius.
    """
    pass

def charger_detect() -> Union[bool, int]:
    """
    Checks what type of charger was detected.

    ### Returns
    - See charging constants for all possible return values. Returns False if it failed to detect a charger.
    """
    pass

def info() -> dict:
    """
    Gets status information about the battery.

    This returns a dictionary of the form:

    ```
    {
        # Battery measurements as documented above.
        'battery_capacity_left': 100
        'temperature': 25.7,
        'charge_current': 248,
        'charge_voltage': 8294,

        # Filtered version of the battery voltage.
        'charge_voltage_filtered': 8287,

        # A list of active errors. See constants given below.
        'error_state': [0],

        # Charging state. See constants given below.
        'charger_state': 2,
    }
    ```
    ### Returns
    - Battery status information.
    """
    pass

# Battery status values
BATTERY_NO_ERROR = 0    #The battery is happy.
BATTERY_HUB_TEMPERATURE_CRITICAL_OUT_OF_RANGE= -1 #The battery temperature is outside of the expected range.
BATTERY_TEMPERATURE_OUT_OF_RANGE= -2 #The battery temperature is outside of the critical range.
BATTERY_TEMPERATURE_SENSOR_FAIL= -3 #The battery temperature sensor is not working.
BATTERY_BAD_BATTERY= -4 #Something is wrong with the battery.
BATTERY_VOLTAGE_TOO_LOW= -5 #The battery voltage is too low.
BATTERY_MISSING= -6 #No battery detected.

#Charger types
USB_CH_PORT_NONE= 0 #No charger detected.
USB_CH_PORT_SDP= 1 #Standard downstream port (typical USB port).
USB_CH_PORT_CDP= 2 #Charging Downstream Port (wall charger).
USB_CH_PORT_DCP= 3 #Dedicated charging port (high current USB port).

#Charging states
CHARGER_STATE_FAIL= -1 #There was a problem charging the battery.
CHARGER_STATE_DISCHARGING= 0 #The battery is discharging.
CHARGER_STATE_CHARGING_ONGOING= 1 #The battery is charging. 
CHARGER_STATE_CHARGING_COMPLETED= 2 #The battery is fully charged.