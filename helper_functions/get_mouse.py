import time
from helper_functions.get_screen import take_screenshot

def on_click(x: int, y: int, button: int, pressed: bool, actions: dict) -> None:
    """Log Mouse Clicks

    Args:
        x (int): X position of the mouse
        y (int): Y position of the mouse
        button (int): Mouse button pressed
        pressed (bool): Whether the mouse button was pressed or released
        actions (dict): Logs Dictionary
    """
    
    action = {
        "by": "mouse",
        "action": "pressed" if pressed else "released",
        "position": (x, y),
        "button": str(button),
        "timestamp": time.time()
    }
    
    actions['actions'].append(action)
    take_screenshot(x - 100, y - 100, x + 100, y + 100)

def on_scroll(x: int, y: int, dx: int, dy: int, actions: dict) -> None:
    """Log Mouse Scrolling

    Args:
        x (int): Start X position of the mouse
        y (int): Start Y position of the mouse
        dx (int): Next X position of the mouse
        dy (int): Next Y position of the mouse
        actions (dict): Logs Dictionary
    """
    
    action = {
        "by": "mouse",
        "action": "scroll",
        "from_position": (x, y),
        "to_position": (dx, dy),
        "timestamp": time.time()
    }
    
    actions['actions'].append(action)

def on_move(x: int, y: int, actions: dict) -> None:
    """Log Mouse Movement

    Args:
        x (int): X position of the mouse after movement
        y (int): Y position of the mouse after movement
        actions (dict): Logs Dictionary
    """
    
    action = {
        "by": "mouse",
        "action": "move",
        "postion": (x, y),
        "timestamp": time.time()
    }
    
    actions['actions'].append(action)

if __name__ == "__main__":
    pass