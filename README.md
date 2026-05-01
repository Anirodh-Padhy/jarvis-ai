# 🤖 Jarvis AI Assistant

A **production-level AI assistant** inspired by Iron Man’s Jarvis, capable of **voice interaction, system automation, AI-powered conversations, mood detection, and face-based security**.

---

## 🚀 Features

### 🎙️ Voice Assistant

* Real-time voice commands
* Speech-to-text + text-to-speech interaction

### 🧠 AI Brain (Local LLM)

* Integrated with **Ollama (local AI models)**
* Handles unknown queries intelligently

### ⚙️ System Automation

* Open applications (Chrome, Notepad, etc.)
* Scroll up/down
* Close tabs/windows
* Execute system-level commands

### 😊 Mood Detection

* Detects user mood from input
* Suggests actions accordingly

### 🔐 Face Recognition Security

* Detects authorized vs unknown user
* Locks system if unknown face detected
* Real-time camera monitoring with visual feedback

### 🖥️ UI Dashboard (Streamlit)

* Command input interface
* Activity logs
* Quick action buttons

---

## 🏗️ Project Structure

```
jarvis-ai/
│
├── app.py                # Streamlit UI
├── main.py               # Voice assistant core
│
├── config/               # Configuration
├── core/                 # Main modules
│   ├── brain/            # AI + NLP
│   ├── automation/       # System control
│   ├── emotion/          # Mood detection
│   ├── security/         # Face recognition
│   ├── voice/            # Speech handling
│   └── utils/            # Logger
│
├── data/                 # Assets (face image)
├── logs/                 # Log files
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/jarvis-ai.git
cd jarvis-ai
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Install Ollama (AI Engine)

Download from: https://ollama.com

Run:

```bash
ollama run phi3
```

---

### 4️⃣ Add Face Image

Place your image:

```
data/my_face.jpg
```

Requirements:

* Clear front face
* Good lighting

---

## ▶️ Usage

### 🔹 Run Voice Assistant

```bash
python main.py
```

---

### 🔹 Run UI Dashboard

```bash
streamlit run app.py
```

---

## 🧪 Example Commands

* “open chrome”
* “scroll down”
* “close tab”
* “what is machine learning”
* “i feel tired”
* “start security”

---

## 📦 Build Executable

```bash
pip install pyinstaller
pyinstaller --onedir main.py
```

---

## ⚠️ Requirements

* Microphone access 🎤
* Camera access 📷
* Ollama running locally 🧠

---

## 🧠 Tech Stack

* Python
* OpenCV
* face_recognition (dlib)
* PyAutoGUI
* SpeechRecognition
* Streamlit
* Ollama (Local LLM)

---

## 🎯 Future Improvements

* Wake word detection (“Hey Jarvis”)
* Multi-user face recognition
* Chat memory
* Mobile integration
* Custom GUI (Electron / PyQt)

---

## 📸 Screenshots (Add Later)

* UI Dashboard
* Face detection window
* Command execution

---

## 🧠 Key Learning

* Real-time AI system integration
* Computer vision + automation
* Local LLM deployment
* Modular architecture design

---

## 👨‍💻 Author

**Anirodh Padhy**

---

## ⭐ Support

If you like this project:

👉 Star the repo
👉 Share it
👉 Fork it

---

## 🏁 Conclusion

This project demonstrates a **full-stack AI system** combining:

* Voice
* Vision
* Automation
* Intelligence

Built with a focus on **real-world usability and scalability** 🚀
