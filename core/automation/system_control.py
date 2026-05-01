import os
import webbrowser
import pyautogui
import time

# 🔹 Open application
def open_app(app_name):
    try:
        os.system(f"start {app_name}")
        return f"Opening {app_name}"
    except:
        return "Failed to open application"

# 🔹 Open any website
def open_website(site):
    webbrowser.open(f"https://{site}.com")
    return f"Opening {site}"

# 🔹 Search anything
def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching for {query}"

# 🔹 Type text (automation)
def type_text(text):
    time.sleep(2)
    pyautogui.write(text, interval=0.05)
    return "Typing completed"

# 🔹 Press key
def press_key(key):
    pyautogui.press(key)
    return f"Pressed {key}"

# 🔹 Lock system (Windows)
def lock_system():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "Locking system"

# 🔽 Scroll down
def scroll_down():
    pyautogui.scroll(-500)
    return "Scrolling down"

# 🔼 Scroll up
def scroll_up():
    pyautogui.scroll(500)
    return "Scrolling up"

# ❌ Close tab / window
def close_tab():
    pyautogui.hotkey('ctrl', 'w')
    return "Closing tab"

# ❌ Close window (stronger)
def close_window():
    pyautogui.hotkey('alt', 'f4')
    return "Closing window"