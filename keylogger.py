import time
from pynput import mouse, keyboard
from helper_functions.get_keyboard import on_release, on_press
from helper_functions.get_mouse import on_click, on_scroll, on_move
from helper_functions.save_data import save_to_json, save_to_text

actions = {
    "timestamp": "",
    "actions": []
}
json_log_file = "log_files/logs.jsonl"
text_log_file = "log_files/logs.txt"

def log_actions() -> None:
    """Log Mouse and Keyboard Actions
    """
    
    global actions
    
    with mouse.Listener(
        on_click=lambda x, y, button, pressed: on_click(x, y, button, pressed, actions), 
        on_scroll=lambda x, y, dx, dy: on_scroll(x, y, dx, dy, actions), 
        on_move=lambda x, y: on_move(x, y, actions)
    ) as mouse_listener, keyboard.Listener(
        on_press=lambda key: on_press(key, actions), 
        on_release=lambda key: on_release(key, actions)
    ) as keyboard_listener:
        
        start_time: time = time.time()
        
        while True:
            current_time: time = time.time()
            elapsed_time: time = current_time - start_time
            
            if elapsed_time >= 5:
                if actions["actions"]:
                    actions['timestamp'] = f"Start_Time {start_time} - End_Time {current_time}"
                
                    save_to_json(json_log_file, actions)
                    save_to_text(text_log_file, actions)
                
                actions = {
                    "timestamp": "",
                    "actions": []
                }
            
            if not mouse_listener.running or not keyboard_listener.running:
                break

def clear_file(filename: str) -> None:
    """Clear the contents of a file

    Args:
        filename (str): File name to be cleared
    """
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("")

if __name__ == '__main__':
    clear_file(json_log_file)
    clear_file(text_log_file)
    
    log_actions()