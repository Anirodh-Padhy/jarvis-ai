def detect_mood(command):
    command = command.lower()

    if any(word in command for word in ["happy", "great", "excited"]):
        return "happy"

    elif any(word in command for word in ["sad", "tired", "depressed"]):
        return "sad"

    elif any(word in command for word in ["angry", "frustrated"]):
        return "angry"

    else:
        return "neutral"