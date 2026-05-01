import datetime
from core.automation.system_control import (
    open_app,
    open_website,
    search_google,
    type_text,
    press_key,
    lock_system 
)
from core.automation.system_control import (
    scroll_down,
    scroll_up,
    close_tab,
    close_window
)

def execute_intent(intent_data):

    intent = intent_data.get("intent")
    value = intent_data.get("value", "")

    # 🔹 OPEN APP / WEBSITE
    if intent == "open_dynamic":
        if "." in value:
            return open_website(value)
        else:
            return open_app(value)

    # 🔹 SEARCH
    elif intent == "search":
        return search_google(value)

    # 🔹 TYPE
    elif intent == "type":
        return type_text(value)

    # 🔹 PRESS KEY
    elif intent == "press":
        return press_key(value)

    # 🔹 LOCK SYSTEM
    elif intent == "lock":
        return lock_system()

    # 🔹 TIME
    elif intent == "time":
        return f"The time is {datetime.datetime.now().strftime('%H:%M')}"

    # 🔹 EXIT
    elif intent == "exit":
        return "exit"
    # 🔽 Scroll down
    elif intent == "scroll_down":
        return scroll_down()

# 🔼 Scroll up
    elif intent == "scroll_up":
        return scroll_up()

# ❌ Close tab
    elif intent == "close_tab":
        return close_tab()

# ❌ Close window
    elif intent == "close_window":
        return close_window()
    # 🔹 UNKNOWN
    return None