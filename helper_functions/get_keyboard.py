import time
from pynput import keyboard

def on_press(key: keyboard.Key, actions: dict) -> None:
    """Log Keyboard Press

    Args:
        key (keyboard.Key): Key pressed by the user
        actions (dict): Logs Dictionary
    """
    
    try:
        action = {
            "by": "keyboard",
            "action": "pressed",
            "key": str(key.char),
            "timestamp": time.time()
        }
        
        actions['actions'].append(action)
    except:
        action = {
            "by": "keyboard",
            "action": "pressed",
            "key": str(key),
            "timestamp": time.time()
        }
        
        actions['actions'].append(action)

def on_release(key: keyboard.Key, actions: dict) -> None | bool:
    """Log Keyboard Release

    Args:
        key (keyboard.Key): Key released by the user
        actions (dict): Logs Dictionary
    
    Returns:
        bool: Whether to stop the listener or not
    """
    
    try:
        action = {
            "by": "keyboard",
            "action": "released",
            "key": str(key.char),
            "timestamp": time.time()
        }
        
        actions['actions'].append(action)
    except:
        action = {
            "by": "keyboard",
            "action": "released",
            "key": str(key),
            "timestamp": time.time()
        }
        
        actions['actions'].append(action)
    
    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    pass