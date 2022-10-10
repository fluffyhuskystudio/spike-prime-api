from typing import Callable, overload

# The Bluetooth module.

@overload
def discoverable() -> int:
    pass

@overload
def discoverable(time: int):
    """
    Gets or sets the Bluetooth classic discoverability state.

    ### Parameters
    - `time` - For how many seconds the hub should be discoverable. During this time, you can find the hub when you search for Bluetooth devices using your computer or phone.

    ### Returns
    - If no argument is given, this returns the remaining number of seconds that the hub is discoverable. Once the hub is no longer discoverable, it returns 0.
    """
    pass

@overload
def rfcomm_connect() -> str:
    pass

@overload
def rfcomm_connect(address: str) -> bool:
    """
    Connects to a Bluetooth Classic MAC address.

    ### Parameters
    - `address` - A string of format aa:bb:cc:dd:ee:ff that represents the MAC address of the Bluetooth Classic device to connect with.

    ### Returns
    - If no argument is given, returns the MAC address that the RFCOMM service is conneted to. If there is no active connection the address is 00:00:00:00:00:00.
    - True if a valid address was given, or False if the address is not a valid MAC address string.
    - The result does not reflect the status of the connection attempt.
    """
    pass

def rfcomm_disconnect() -> None:
    """
    Disconnects an active RFCOMM channel

    The result does not reflect the status of the disconnection attempt.
    """
    pass

def info() -> dict:
    """
    Gets a dictionary of the form:

    ```
    {
        # The Bluetooth device MAC address.
        'mac_addr': '38:0B:3C:A2:E1:E4',

        # The Bluetooth device UUID.
        'device_uuid': '03970000-1800-3500-1551-383235373836'

        # The outgoing service UUID.
        'service_uuid': '',

        # Bluetooth name of the device.
        'name': 'LEGO Hub 38:0B:3C:A2:E1:E4',

        # iPod Accessory Protocol (iAP) status dictionary.
        'iap': {
            'device_version': 7,
            'authentication_revision': 1,
            'device_id': -1,
            'certificate_serial_no': '54D2891DEC5E5104F7132BC3059365CB',
            'protocol_major_version': 3,
            'protocol_minor_version': 0
        },

        # A list of devices that the hub has been connected to.
        'known_devices': ['8C:8D:28:2D:E0:0F', 'E8:6D:CB:77:64:D5'],
    }
    ```
    ### Returns
    - Bluetooth subsystem information dictionary similar to the example above, or None if the Bluetooth subsystem is not running.
    - The MAC address in known_devices is reversed for Windows devices.
    """
    pass

def forget(address) -> bool:
    """
    Removes a device from the list of known Bluetooth devices.

    ### Parameters
    - `address` - Bluetooth address of the form '01:23:45:67:89:AB'.

    ### Returns
    - True if a valid address was given, or False if not.
    - Functions for the LEGO Wireless Protocol
    """
    pass

@overload
def lwp_advertise() -> int:
    pass

@overload
def lwp_advertise(timeout: int):
    """
    Gets or sets the Bluetooth Low Energy LEGO Wireless protocol advertising state.

    ### Parameters
    - `time` - For how many seconds the hub should advertise the LEGO Wireless Protocol. During this time, you can find the hub when you search for Bluetooth devices using your computer or phone.

    ### Returns
    - If no argument is given, this returns the remaining number of seconds that the hub will advertise. Once the hub is no longer advertising, it returns 0.
    """
    pass

@overload
def lwp_bypass() -> bool:
    pass

@overload
def lwp_bypass(bypass: bool):
    """
    Controls whether the LEGO Wireless Protocol is bypassed when using Bluetooth Low Energy.

    ### Parameters
    - `bypass` - Choose True to bypass the LEGO Wireless protocol or choose False to enable it.

    ### Returns
    - If no argument is given, this returns the current bypass state.
    """
    pass

def lwp_monitor(self, handler: Callable[[int], None]):
    """
    Sets the callback function that is called when a connection is made using the LEGO Wireless Protocol.

    The function must accept one argument, which provides information about the incoming connection.

    ### Parameters
    - `handler` - Callable function that takes one argument. Choose None to disable the callback.
    """
    pass

