## SpyWare - Advanced Python-based Spying Tool

**SpyWare** is a powerful Python-based tool designed for advanced cybersecurity applications. It offers real-time monitoring of keyboard and mouse activity on the target system, ensuring comprehensive data capture with efficient code structures.

**Features:**

* **Real-time Monitoring:** Captures keyboard (keystrokes & releases) and mouse (clicks, scrolls, movements) activity.
* **Efficient Codebase:** Maintains low resource consumption while delivering comprehensive logging capabilities.
* **Detailed Logging:** 
    * JSONL files (`/log_files/logs.jsonl`) for machine-readable, structured logs.
    * Plain text files (`/log_files/logs.txt`) with clear visual separation for human readability.
* **Customizable Triggers:** Define conditions (e.g., Escape key) to stop data logging.
* **Modular Design:**
    * `keylogger.py`: Handles all keystroke and mouse events.
    * `helper_functions/`:
        * `get_mouse.py`: Captures mouse events.
        * `get_keyboard.py`: Focuses on key releases and custom stopping mechanisms.
        * `get_screen.py`: Focuses on mouse clicks to create a screenshot with red highlighted region signifying where mouse clicked
    * `save_data/`: Responsible for writing captured data to both JSON and text files.
* **Clear Documentation:** Comments throughout the codebase enhance use and contribution by other developers.

**Purpose:**

**SpyWare** is primarily designed for ethical cybersecurity applications or research activities. 
**Always ensure your usage adheres to strict ethical guidelines.**

I am just currently exploring the capabilities of a Spyware to understand how it works and what is possible with it.
