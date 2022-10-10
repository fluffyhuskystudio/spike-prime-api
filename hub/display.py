from __future__ import annotations
from typing import Callable, Iterable

"""
The Image class lets you create and modify images that you can show on the hub matrix display using the hub.display module.
"""
class Image:
    
    def __init__(self, *args):
        """
        Create a new image object for use with the hub.display.show() function.

        ```
        Image(string: str)
        Image(width: int, height: int)
        Image(width: int, height: int, buffer: bytes)
        ```

        You can use one of the signatures above to initialize an image, depending on what you need.

        ### Parameters
        
        - `string` - String of the form "00900:09990:99999:09990:09090:", representing the brightness of each pixel (0 to 9). Pixels are listed row by row, separated by a colon (:) or line break (\\n).
        - `width` - Number of pixels in one row of the new image.
        - `height` - Number of pixels in one column of the new image.
        - `buffer` - Bytes representing the brightness values of each pixel in the new image. The buffer size must be equal to width * height. If you give a with and height but no buffer, you will get an image where all pixels are zero.
        """
        pass

    def width(self) -> int:
        """
        Gets the width of the image as a number of pixels.
        """
        pass

    def height(self) -> int:
        """
        Gets the width of the image as a number of pixels.
        """
        pass

    def shift_left(n: int) -> 'Image':
        """
        Shifts the image to the left.

        ### Parameters
        - `n1 - By how many pixels to shift the image.

        ### Returns
        - A new, shifted image.
        """
        pass

    def shift_right(n: int) -> 'Image':
        """
        Shifts the image to the right.

        ### Parameters
        - `n` - By how many pixels to shift the image.

        ### Returns
        - A new, shifted image.
        """
        pass

    def shift_up(n: int) -> 'Image':
        """
        Shifts the image up.

        ### Parameters
        - `n` - By how many pixels to shift the image.

        ### Returns
        - A new, shifted image.
        """
        pass

    def shift_down(n: int) -> 'Image':
        """
        Shifts the image down.

        ### Parameters
        - `n` - By how many pixels to shift the image.

        ### Returns
        - A new, shifted image.
        """
        pass

    def get_pixel(x: int, y: int, brightness: int) -> int:
        """
        Gets the brightness of one pixel in the image.

        ### Parameters
        - `x` - Pixel position counted from the left, starting at zero.
        - `y` - Pixel position counted from the top, starting at zero.

        ### Returns
        - Brightness (0-9) of the requested pixel.
        """
        pass

    def set_pixel(x: int, y: int, brightness: int) -> None:
        """
        Sets the brightness of one pixel in the image.

        ### Parameters
        - `x` - Pixel position counted from the left, starting at zero.
        - `y` - Pixel position counted from the top, starting at zero.
        - `brightness` - Brightness between 0 (fully off) and 9 (fully on).

        ### Raises
        - `ValueError` - If x or y are negative or larger than the image size.
        - `TypeError` - If you try to modify a built-in image such as HEART.
        """
        pass

    ANGRY: Image
    ARROW_E: Image
    ARROW_N: Image
    ARROW_NE: Image
    ARROW_NW: Image
    ARROW_S: Image
    ARROW_SE: Image
    ARROW_SW: Image
    ARROW_W: Image
    ASLEEP: Image
    BUTTERFLY: Image
    CHESSBOARD: Image
    CLOCK1: Image
    CLOCK2: Image
    CLOCK3: Image
    CLOCK4: Image
    CLOCK5: Image
    CLOCK6: Image
    CLOCK7: Image
    CLOCK8: Image
    CLOCK9: Image
    CLOCK10: Image
    CLOCK11: Image
    CLOCK12: Image
    CONFUSED: Image
    COW: Image
    DIAMOND: Image
    DIAMOND_SMALL: Image
    DUCK: Image
    FABULOUS: Image
    GHOST: Image
    GIRAFFE: Image
    GO_DOWN: Image
    GO_LEFT: Image
    GO_RIGHT: Image
    GO_UP: Image
    HAPPY: Image
    HEART: Image
    HEART_SMALL: Image
    HOUSE: Image
    MEH: Image
    MUSIC_CROTCHET: Image
    MUSIC_QUAVER: Image
    MUSIC_QUAVERS: Image
    NO: Image
    PACMAN: Image
    PITCHFORK: Image
    RABBIT: Image
    ROLLERSKATE: Image
    SAD: Image
    SILLY: Image
    SKULL: Image
    SMILE: Image
    SNAKE: Image
    SQUARE: Image
    SQUARE_SMALL: Image
    STICKFIGURE: Image
    SURPRISED: Image
    SWORD: Image
    TARGET: Image
    TORTOISE: Image
    TRIANGLE: Image
    TRIANGLE_LEFT: Image
    TSHIRT: Image
    UMBRELLA: Image
    XMAS: Image
    YES: Image
    ALL_CLOCKS: Image
    ALL_ARROWS: Image

#Built-in images
Image.ANGRY = Image('90009:09090:00000:99999:90909:')
Image.ARROW_E = Image('00900:00090:99999:00090:00900:')
Image.ARROW_N = Image('00900:09990:90909:00900:00900:')
Image.ARROW_NE = Image('00999:00099:00909:09000:90000:')
Image.ARROW_NW = Image('99900:99000:90900:00090:00009:')
Image.ARROW_S = Image('00900:00900:90909:09990:00900:')
Image.ARROW_SE = Image('90000:09000:00909:00099:00999:')
Image.ARROW_SW = Image('00009:00090:90900:99000:99900:')
Image.ARROW_W = Image('00900:09000:99999:09000:00900:')
Image.ASLEEP = Image('00000:99099:00000:09990:00000:')
Image.BUTTERFLY = Image('99099:99999:00900:99999:99099:')
Image.CHESSBOARD = Image('09090:90909:09090:90909:09090:')
Image.CLOCK1 = Image('00090:00090:00900:00000:00000:')
Image.CLOCK2 = Image('00000:00099:00900:00000:00000:')
Image.CLOCK3 = Image('00000:00000:00999:00000:00000:')
Image.CLOCK4 = Image('00000:00000:00900:00099:00000:')
Image.CLOCK5 = Image('00000:00000:00900:00090:00090:')
Image.CLOCK6 = Image('00000:00000:00900:00900:00900:')
Image.CLOCK7 = Image('00000:00000:00900:09000:09000:')
Image.CLOCK8 = Image('00000:00000:00900:99000:00000:')
Image.CLOCK9 = Image('00000:00000:99900:00000:00000:')
Image.CLOCK10 = Image('00000:99000:00900:00000:00000:')
Image.CLOCK11 = Image('09000:09000:00900:00000:00000:')
Image.CLOCK12 = Image('00900:00900:00900:00000:00000:')
Image.CONFUSED = Image('00000:09090:00000:09090:90909:')
Image.COW = Image('90009:90009:99999:09990:00900:')
Image.DIAMOND = Image('00900:09090:90009:09090:00900:')
Image.DIAMOND_SMALL = Image('00000:00900:09090:00900:00000:')
Image.DUCK = Image('09900:99900:09999:09990:00000:')
Image.FABULOUS = Image('99999:99099:00000:09090:09990:')
Image.GHOST = Image('99999:90909:99999:99999:90909:')
Image.GIRAFFE = Image('99000:09000:09000:09990:09090:')
Image.GO_DOWN = Image('00000:99999:09990:00900:00000:')
Image.GO_LEFT = Image('00090:00990:09990:00990:00090:')
Image.GO_RIGHT = Image('09000:09900:09990:09900:09000:')
Image.GO_UP = Image('00000:00900:09990:99999:00000:')
Image.HAPPY = Image('00000:09090:00000:90009:09990:')
Image.HEART = Image('09090:99999:99999:09990:00900:')
Image.HEART_SMALL = Image('00000:09090:09990:00900:00000:')
Image.HOUSE = Image('00900:09990:99999:09990:09090:')
Image.MEH = Image('09090:00000:00090:00900:09000:')
Image.MUSIC_CROTCHET = Image('00900:00900:00900:99900:99900:')
Image.MUSIC_QUAVER = Image('00900:00990:00909:99900:99900:')
Image.MUSIC_QUAVERS = Image('09999:09009:09009:99099:99099:')
Image.NO = Image('90009:09090:00900:09090:90009:')
Image.PACMAN = Image('09999:99090:99900:99990:09999:')
Image.PITCHFORK = Image('90909:90909:99999:00900:00900:')
Image.RABBIT = Image('90900:90900:99990:99090:99990:')
Image.ROLLERSKATE = Image('00099:00099:99999:99999:09090:')
Image.SAD = Image('00000:09090:00000:09990:90009:')
Image.SILLY = Image('90009:00000:99999:00909:00999:')
Image.SKULL = Image('09990:90909:99999:09990:09990:')
Image.SMILE = Image('00000:00000:00000:90009:09990:')
Image.SNAKE = Image('99000:99099:09090:09990:00000:')
Image.SQUARE = Image('99999:90009:90009:90009:99999:')
Image.SQUARE_SMALL = Image('00000:09990:09090:09990:00000:')
Image.STICKFIGURE = Image('00900:99999:00900:09090:90009:')
Image.SURPRISED = Image('09090:00000:00900:09090:00900:')
Image.SWORD = Image('00900:00900:00900:09990:00900:')
Image.TARGET = Image('00900:09990:99099:09990:00900:')
Image.TORTOISE = Image('00000:09990:99999:09090:00000:')
Image.TRIANGLE = Image('00000:00900:09090:99999:00000:')
Image.TRIANGLE_LEFT = Image('90000:99000:90900:90090:99999:')
Image.TSHIRT = Image('99099:99999:09990:09990:09990:')
Image.UMBRELLA = Image('09990:99999:00900:90900:09900:')
Image.XMAS = Image('00900:09990:00900:09990:99999:')
Image.YES = Image('00000:00009:00090:90900:09000:')

#Built-in tuples of images
Image.ALL_CLOCKS = (Image('00900:00900:00900:00000:00000:'), Image('00090:00090:00900:00000:00000:'), Image('00000:00099:00900:00000:00000:'), Image('00000:00000:00999:00000:00000:'), Image('00000:00000:00900:00099:00000:'), Image('00000:00000:00900:00090:00090:'), Image('00000:00000:00900:00900:00900:'), Image('00000:00000:00900:09000:09000:'), Image('00000:00000:00900:99000:00000:'), Image('00000:00000:99900:00000:00000:'), Image('00000:99000:00900:00000:00000:'), Image('09000:09000:00900:00000:00000:'))
Image.ALL_ARROWS = (Image('00900:09990:90909:00900:00900:'), Image('00999:00099:00909:09000:90000:'), Image('00900:00090:99999:00090:00900:'), Image('90000:09000:00909:00099:00999:'), Image('00900:00900:90909:09990:00900:'), Image('00009:00090:90900:99000:99900:'), Image('00900:09000:99999:09000:00900:'), Image('99900:99000:90900:00090:00009:'))


"""
The display module lets you control the light matrix display on the hub.
"""

def clear():
    """
    Turns off all the pixels.
    """
    pass

def rotation(rotation: int) -> None:
    """
    Rotates the display clockwise relative to its current orientation.

    DEPRECATION WARNING - In the next release this is a do-nothing operation. Use the def align() API instead!

    Following the next release this call will be removed.
    """
    pass

def align() -> int:
    pass

def align(face: int) -> int:
    """
    Rotates the display by aligning the top with the given face of the hub.

    ### Parameters
    - `face` - Choose hub.FRONT, hub.BACK, hub.LEFT, or hub.RIGHT.

    ### Returns
    - The new or current alignment.
    """
    pass

def invert() -> bool:
    pass

def invert(invert: bool) -> bool:
    """
    Inverts all pixels. This affects what is currently displayed, as well as everything you display afterwards.

    In the inverted state, the brightness of each pixel is the opposite of the normal state. If a pixel has brightness b, it will be displayed with brightness 9 - b.

    ### Parameters
    - `invert` - Choose True to activate the inverted state. Choose False to restore the normal state.

    ### Returns
    - The new or current inversion state.
    """
    pass

def callback(self, function: Callable[[int], None]) -> None:
    """
    Sets the callback function that is called when a display operation is completed or interrupted.

    The function must accept one argument, which indicates why the callback was called. It will receive 0 if a display operation completed successfully, or 1 if it was interrupted.

    ### Parameters
    - `function` - Callable function that takes one argument. Choose None to disable the callback.
    """
    pass

def pixel(x: int, y: int) -> int:
    pass

def pixel(x: int, y: int, brightness: int) -> None:
    """
    Gets or sets the brightness of one pixel.

    ### Parameters
    - `x` - Pixel position counted from the left, starting at zero.
    - `y` - Pixel position counted from the top, starting at zero.
    - `brightness` - Brightness between 0 (fully off) and 9 (fully on).

    ### Returns
    - If no brightness is given, this returns the brightness of the selected pixel. Otherwise it returns None.
    """
    pass

def show(image: Image) -> None:
    pass

def show(image: Iterable[Image], delay=400, level=9, clear=False, wait=True, loop=False, fade=0) -> None:
    """
    Shows an image or a sequence of images.

    Except for image, all arguments must be specified as keywords.

    ### Parameters
    - `image` - The image or iterable of images to be displayed.

    ### Keyword Arguments
    - `delay` - Delay between each image in the iterable.
    - `level` - Scales the brightness of each pixel in and image or character to a value between 0 (fully off) and 9 (fully on).
    - `clear` - Choose `True` to clear the display after showing the last image in the iterable.
    - `wait` - Choose `True` to block your program until all images are shown. Choose `False` to show all images in the background while your program continues.
    - `loop` - Choose `True` repeat the sequence of images for ever. Choose `False` to show it only once.
    - `fade` -

    Sets the transitional behavior between images in the sequence:

    The image will appear immediately.

    The image will appear immediately.

    The image fades out while the next image fades in.

    Images will scroll to the right.

    Images will scroll to the left.

    Images will fade in, starting from an empty display.

    Images will fade out, starting from the original image.
    """
    pass