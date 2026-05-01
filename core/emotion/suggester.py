def suggest_task(mood):

    if mood == "happy":
        return "You seem happy. Try working on creative tasks or coding."

    elif mood == "sad":
        return "You seem low. Maybe take a break or listen to music."

    elif mood == "angry":
        return "You seem stressed. Take a short break or go for a walk."

    else:
        return "You seem neutral. You can continue your regular work."