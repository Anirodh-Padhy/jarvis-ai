def detect_intent(command):
    command = command.lower().strip()

    # 🔴 EXIT
    if "exit" in command or "stop" in command or "bye" in command:
        return {"intent": "exit"}

    # 🔹 SEARCH
    if "search for" in command:
        query = command.replace("search for", "").strip()
        return {"intent": "search", "value": query}

    # 🔹 OPEN (dynamic)
    if "open" in command:
        value = command.replace("open", "").strip()
        return {"intent": "open_dynamic", "value": value}

    # 🔹 TYPE TEXT
    if "type" in command:
        text = command.replace("type", "").strip()
        return {"intent": "type", "value": text}

    # 🔹 PRESS KEY
    if "press" in command:
        key = command.replace("press", "").strip()
        return {"intent": "press", "value": key}

    # 🔹 LOCK SYSTEM
    if "lock system" in command:
        return {"intent": "lock"}

    # 🔹 TIME
    if "time" in command:
        return {"intent": "time"}
    # 🔽 Scroll down
    if "scroll down" in command:
        return {"intent": "scroll_down"}

# 🔼 Scroll up
    if "scroll up" in command:
        return {"intent": "scroll_up"}

# ❌ Close tab
    if "close tab" in command:
        return {"intent": "close_tab"}

# ❌ Close window
    if "close window" in command:
        return {"intent": "close_window"}
    
    # 🔹 DEFAULT
    return {"intent": "unknown"}
    