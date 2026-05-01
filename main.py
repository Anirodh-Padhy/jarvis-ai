from core.voice.listen import listen
from core.voice.speak import speak
from core.brain.intent_parser import detect_intent
from commands.basic_commands import execute_intent
from core.brain.ai_chat import ask_ai

from core.emotion.mood_detector import detect_mood
from core.emotion.suggester import suggest_task
from core.security.face_lock import monitor_face


def run_jarvis():
    speak("Hello, Boss")

    while True:
        command = listen()

        # 🔹 Skip empty input
        if not command:
            continue

        # 🔹 Normalize command
        command = command.lower()

        # ================= MOOD SYSTEM =================
        if "i feel" in command:
            mood = detect_mood(command)
            suggestion = suggest_task(mood)
            speak(suggestion)
            continue

        # ================= SECURITY SYSTEM =================
        if "start security" in command:
            speak("Starting face monitoring")
            monitor_face()
            continue

        # ================= INTENT DETECTION =================
        intent_data = detect_intent(command)

        # ================= SAFETY FILTER =================
        blocked_words = ["delete", "format", "hack"]

        if any(word in command for word in blocked_words):
            speak("I cannot perform that action.")
            continue

        # ================= CONFIRMATION SYSTEM =================
        dangerous_intents = ["lock"]

        if intent_data["intent"] in dangerous_intents:
            speak("Are you sure?")
            confirm = listen()

            confirm_words = ["yes", "ok", "okay", "confirm", "sure"]
            cancel_words = ["no", "cancel", "stop"]

            if any(word in confirm for word in cancel_words):
                speak("Action cancelled")
                continue

            if not any(word in confirm for word in confirm_words):
                speak("I didn't understand, cancelling for safety.")
                continue

        # ================= EXECUTE COMMAND =================
        result = execute_intent(intent_data)

        # ================= AI FALLBACK =================
        if result is None:
            result = ask_ai(command)

        # ================= EXIT =================
        if result == "exit":
            speak("Goodbye")
            break

        # ================= SPEAK =================
        if result:
            speak(result)


if __name__ == "__main__":
    run_jarvis()
    