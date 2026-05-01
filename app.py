import streamlit as st
from core.voice.speak import speak
from core.brain.intent_parser import detect_intent
from commands.basic_commands import execute_intent
from core.brain.ai_chat import ask_ai
from core.emotion.mood_detector import detect_mood
from core.emotion.suggester import suggest_task
from core.security.face_lock import monitor_face

st.set_page_config(page_title="Jarvis AI", layout="centered")

st.title("🤖 Jarvis AI Assistant")
password = st.text_input("Enter Password", type="password")

if password != "1234":
    st.stop()
# ================= SESSION STATE =================
if "logs" not in st.session_state:
    st.session_state.logs = []

# ================= INPUT =================
command = st.text_input("Enter command (or speak via main.py):")

# ================= BUTTON =================
if st.button("Run Command"):

    if command:

        st.session_state.logs.append(f"You: {command}")

        command = command.lower()

        # 🧠 Mood system
        if "i feel" in command:
            mood = detect_mood(command)
            result = suggest_task(mood)

        # 🔐 Security
        elif "start security" in command:
            result = "Starting security system..."
            monitor_face()

        else:
            intent_data = detect_intent(command)

            result = execute_intent(intent_data)

            if result is None:
                result = ask_ai(command)

        st.session_state.logs.append(f"Jarvis: {result}")
        speak(result)

# ================= QUICK ACTIONS =================
st.subheader("⚡ Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Open Chrome"):
        speak("Opening Chrome")
        execute_intent({"intent": "open_dynamic", "value": "chrome"})

with col2:
    if st.button("Scroll Down"):
        execute_intent({"intent": "scroll_down"})

with col3:
    if st.button("Lock System"):
        monitor_face()

# ================= LOGS =================
st.subheader("📜 Activity Logs")

for log in st.session_state.logs[::-1]:
    st.write(log)