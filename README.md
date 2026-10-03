<div align="center">

# 🎙️ Voice Assistant using Python

### A Beginner-Friendly Python Project

</div>

## 📖 About This Project

A **Voice Assistant** is a program that listens to your voice (or text) commands and responds intelligently — just like Siri, Alexa, or Google Assistant!

In this project, you will build your very own voice assistant using **Python** from scratch. It can:
- Understand what you say through a microphone
- Speak back to you using a text-to-speech engine
- Search Wikipedia, open websites, tell time, crack jokes, and much more

This project is designed for **beginners** — no prior AI or ML experience is needed. Every function is clearly explained so you can follow along and understand each line of code.

---

## 🎓 What You Will Learn

By completing this project, you will understand:

| Concept | Library Used |
|---------|-------------|
| Text-to-Speech (making Python talk) | `pyttsx3` |
| Speech Recognition (making Python listen) | `SpeechRecognition` |
| Fetching data from Wikipedia | `wikipedia` |
| Opening websites from Python | `webbrowser` |
| Working with date & time | `datetime` |
| Generating jokes programmatically | `pyjokes` |
| Reading/writing files in Python | built-in `open()` |
| Creating a menu-driven program | `if/elif/else` |

---

## ✨ Features

| # | Feature | Command Example |
|---|---------|----------------|
| 1 | Greet user based on time of day | *(automatic on start)* |
| 2 | Search Wikipedia | `wikipedia machine learning` |
| 3 | Open popular websites | `open youtube` |
| 4 | Tell current time | `time` |
| 5 | Tell today's date | `date` |
| 6 | Tell a random joke | `joke` |
| 7 | Save a note to file | `note study AI tonight` |
| 8 | Basic calculator | `calculate 25 plus 75` |
| 9 | Help menu | `help` |
| 10 | Exit gracefully | `bye` or `exit` |

---

## 📁 Project Structure

```
voice-assistant-python/
│
├── voice_assistant.py     ← Main Python program (all the code is here)
├── requirements.txt       ← List of Python libraries to install
├── output_examples.md     ← Sample outputs for reference
├── my_notes.txt           ← Created automatically when you save a note
└── README.md              ← This file (documentation)
```

---

## 📚 Libraries Used

| Library | Purpose | Install Command |
|---------|---------|----------------|
| `pyttsx3` | Converts text to speech (offline, works without internet) | `pip install pyttsx3` |
| `SpeechRecognition` | Converts your voice to text using Google Speech API | `pip install SpeechRecognition` |
| `wikipedia` | Searches and fetches Wikipedia summaries | `pip install wikipedia` |
| `pyjokes` | Returns random programming/general jokes | `pip install pyjokes` |
| `PyAudio` | Required to access the microphone | `pip install PyAudio` |
| `webbrowser` | Opens URLs in the browser | *(built-in, no install needed)* |
| `datetime` | Gets current date and time | *(built-in, no install needed)* |
| `os` | Interacts with the operating system | *(built-in, no install needed)* |

---

## 🔧 Prerequisites

Before starting, make sure you have:

- ✅ **Python 3.8 or higher** installed on your computer
- ✅ **pip** (Python package manager) available
- ✅ **Internet connection** (for speech recognition via Google API and Wikipedia)
- ✅ A **microphone** (optional — the project also supports text input mode)

**Check your Python version:**
```bash
python --version
```
You should see something like `Python 3.10.0` or higher.

---

## 🚀 Step-by-Step Installation Guide

Follow these steps carefully. Do them **in order**.

---

### Step 1 — Download or Clone the Project

**Option A: Download ZIP**
1. Click the green **Code** button on this GitHub page
2. Click **Download ZIP**
3. Extract the ZIP file to a folder on your desktop

**Option B: Clone using Git**
```bash
git clone https://github.com/PRINCE77-UI/voice-assistant.git
```

---

### Step 2 — Open the Project Folder

Open your **terminal** (Command Prompt on Windows / Terminal on Mac/Linux) and navigate to the project folder:

```bash
cd voice-assistant
```

> 💡 **Tip for Windows users:** You can hold `Shift` and right-click inside the folder, then select "Open PowerShell window here".

---

### Step 3 — (Recommended) Create a Virtual Environment

A virtual environment keeps your project's libraries separate from other Python projects.

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate it — Windows:
venv\Scripts\activate

# Activate it — Mac/Linux:
source venv/bin/activate
```

After activation, you will see `(venv)` at the beginning of your terminal line.

---

### Step 4 — Install All Required Libraries

Install all dependencies at once using `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install: `pyttsx3`, `SpeechRecognition`, `wikipedia`, `pyjokes`, and `PyAudio`.

> ⚠️ **PyAudio installation issue on Windows?** If `pip install PyAudio` fails, try this instead:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

> ⚠️ **PyAudio issue on Mac?** First install PortAudio, then PyAudio:
> ```bash
> brew install portaudio
> pip install pyaudio
> ```

---

### Step 5 — Verify Installation

Run this quick check to confirm everything is installed:

```bash
python -c "import pyttsx3; import speech_recognition; import wikipedia; import pyjokes; print('All libraries installed successfully!')"
```

Expected output:
```
All libraries installed successfully!
```

---

## ▶️ How to Run the Project

Once installation is complete, run the assistant with:

```bash
python voice_assistant.py
```

You will see a startup screen like this:

```
   Voice Assistant — Gen AI Innovations

  Choose input mode:
  [1] Voice (requires microphone)
  [2] Text  (keyboard input)

  Enter 1 or 2:
```

- **Type `1`** to use voice commands (requires a working microphone)
- **Type `2`** to use text/keyboard input (great for testing)

> 💡 **Recommendation for beginners:** Start with mode `2` (text input) to test all features first, then switch to mode `1` for voice.

---

## 🔍 How the Code Works

Here is a simple explanation of each function in `voice_assistant.py`:

### `init_engine()`
Starts and configures the Text-to-Speech (TTS) engine. Sets voice speed, volume, and gender.

```python
engine = pyttsx3.init()
engine.setProperty('rate', 170)    # 170 words per minute
engine.setProperty('volume', 1.0)  # Full volume
```

### `speak(engine, text)`
Makes the assistant say something out loud AND prints it to the screen.

```python
speak(engine, "Hello! How can I help you?")
# → prints: 🤖 Assistant: Hello! How can I help you?
# → also speaks it aloud
```

### `wish_user(engine)`
Checks the current hour and greets you appropriately:
- Hour < 12 → "Good Morning!"
- Hour 12–18 → "Good Afternoon!"
- Hour > 18 → "Good Evening!"

### `take_command_voice(engine)`
Turns on the microphone, listens for speech, and uses **Google Speech API** to convert it to text.

### `take_command_text()`
Simply reads keyboard input — no microphone needed. Perfect for testing.

### `search_wikipedia(engine, query)`
Uses the `wikipedia` library to search any topic and returns a 2-sentence summary.

### `open_website(engine, site_name)`
Has a built-in dictionary of websites. Say `open youtube` and it opens `https://www.youtube.com`.

### `tell_time(engine)` / `tell_date(engine)`
Uses Python's `datetime` module to get and speak the current time and date.

### `tell_joke(engine)`
Uses `pyjokes` to fetch a random joke and speaks it.

### `take_note(engine, note_text)`
Writes your note to `my_notes.txt` with a timestamp.

### `calculate(engine, expression)`
Converts spoken math words to operators and evaluates:
- `"plus"` → `"+"`
- `"minus"` → `"-"`
- `"times"` → `"*"`
- `"divided by"` → `"/"`

### `run_assistant()`
The **main loop** — keeps running until you say "exit" or "bye".

---

## 💻 Sample Output Examples

See [output_examples.md](output_examples.md) for the full list.

Here are a few quick examples:

**Wikipedia Search:**
```
⌨️  You: wikipedia python programming

🤖 Assistant: Searching Wikipedia for python programming...
🤖 Assistant: According to Wikipedia: Python is a high-level, general-purpose
              programming language. Its design philosophy emphasizes code
              readability with the use of significant indentation.
```

**Calculator:**
```
⌨️  You: calculate 25 plus 75
🤖 Assistant: The answer is 100.
```

**Joke:**
```
⌨️  You: joke
🤖 Assistant: Why do Java developers wear glasses? Because they don't C#!
```

**Exit:**
```
⌨️  You: bye
🤖 Assistant: Goodbye! Have a great day. This is your Gen AI Innovations
              Voice Assistant signing off.
👋 Session ended. Thank you for using  Gen AI Innovations Voice Assistant!
```

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'pyttsx3'` | Run `pip install pyttsx3` |
| `ModuleNotFoundError: No module named 'pyaudio'` | See Step 4 above for OS-specific fix |
| `OSError: [Errno -9996]` (no microphone found) | Use text mode (press `2` at startup) |
| `Could not request results from Google Speech` | Check your internet connection |
| Wikipedia returns wrong result | Add more words to be specific, e.g., `wikipedia Albert Einstein physicist` |
| No sound / TTS not working | Check system volume; try restarting Python |

---

## 🔮 Possible Extensions

Once you finish this project, here are ideas to make it even better:

- 🌦️ **Weather**: Integrate OpenWeatherMap API to get weather updates
- 📧 **Email**: Use `smtplib` to send emails by voice
- 🎵 **Music Player**: Use `pygame` to play local music files
- 📰 **News Headlines**: Use a news API to read today's top headlines
- 🌐 **Custom web search**: Perform Google searches automatically
- 🧠 **AI Chat**: Connect to Claude or GPT API for intelligent conversations
- 🔔 **Reminders/Alarms**: Use `schedule` library to set reminders

---

<div align="center">

**⭐ If this project helped you learn, please give it a star on GitHub! ⭐**

</div>
