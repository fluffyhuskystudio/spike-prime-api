from typing import Tuple, overload
from hub import port, battery, bluetooth, button, display, motion, sound, supervision
from hub.display import Image

__version__  = 'v1.0.0.0000-0000000'
config  = {}

TOP = 0
FRONT = 1
RIGHT = 2
BOTTOM = 3
BACK = 4
LEFT = 5

def info() -> dict:
    pass

def status() -> dict:
    pass

def temperature() -> float:
    pass

@overload
def power_off(fast=True, restart=False):
    pass

@overload
def power_off(timeout=0):
    pass

def repl_restart(restart: bool):
    pass

@overload
def led(color: int):
    pass

@overload
def led(red: int, green: int, blue: int):
    pass

@overload
def led(color: Tuple[int, int, int]):
    pass

def file_transfer(filename: str, filesize: int, packetsize=1000, timeout=2000, mode=None):
    pass


