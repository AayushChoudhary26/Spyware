import json

def save_to_json(filename: str, actions_log: dict) -> None:
    """Save Keyboard and Mouse logs to a JSON file

    Args:
        filename (str): Log file name
        actions_log (dict): Mouse and Keyboard logs
    """
    
    with open(filename, 'a', encoding='utf-8') as log_file:
        json.dump(actions_log, log_file, indent=4)
        log_file.write('\n')

def save_to_text(filename: str, actions_log: dict) -> None:
    """Save Keyboard and Mouse logs to a text file

    Args:
        filename (str): Log file name
        actions_log (_type_): Mouse and Keyboard logs
    """
    
    with open(filename, 'a', encoding='utf-8') as log_file:
        log_file.write("-"*10 + ">")
        log_file.write(f"Timestamp: {actions_log['timestamp']}\n")
        
        for i in range(len(actions_log['actions'])):
            for key, value in actions_log['actions'][i].items():
                log_file.write(f"{key}: {value}\n")
        
        log_file.write("<" + "-"*10)
        log_file.write('\n\n')
    
if __name__ == "__main__":
    pass