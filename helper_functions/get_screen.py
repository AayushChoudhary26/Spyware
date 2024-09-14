import time
import pyautogui
from PIL import Image, ImageDraw

def take_screenshot(start_x: int, start_y: int, width: int, height: int, filepath: str = "Screenshots/") -> None:
    """Take Screenshot of the specified region

    Args:
        start_x (int): Screenshot start X position
        start_y (int): Screenshot start Y position
        width (int): Screenshot width
        height (int): Screenshot height
    """
    
    filename = filepath + "screenshot_" + str(time.time()) + ".png"
    
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

    image = Image.open(filename)
    draw = ImageDraw.Draw(image)

    draw.rectangle((start_x, start_y, width, height), fill=None, outline="red", width=2)
    image.save(filename)

if __name__ == "__main__":
    pass