import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import pyjokes
import os
import time


def init_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)

    voices = engine.getProperty('voices')
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)

    return engine


def speak(engine, text):
    print(f"\n  🤖 Assistant: {text}\n")
    engine.say(text)
    engine.runAndWait()


def wish_user(engine):
    hour = datetime.datetime.now().hour

    if hour < 12:
        greeting = "Good Morning!"
    elif hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"

    speak(engine, f"{greeting} I am your Voice Assistant, powered by  Gen AI Innovations. How can I help you today?")


def take_command_voice(engine):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n  🎤 Listening... (speak now)")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            # listen() ko try block ke andar daal diya taaki WaitTimeoutError catch ho sake
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            print("  ⏳ Recognizing speech...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"  🗣️️  You said: {query}")
            return query.lower()

        except sr.WaitTimeoutError:
            speak(engine, "No speech detected. Please try again.")
            return "none"

        except sr.UnknownValueError:
            speak(engine, "Sorry, I didn't catch that. Please say it again.")
            return "none"

        except sr.RequestError:
            speak(engine, "Network error. Please check your internet connection.")
            return "none"


def take_command_text():
    query = input("  ⌨️  You (type command): ")
    return query.lower().strip()


def search_wikipedia(engine, query):
    speak(engine, f"Searching Wikipedia for {query}...")

    try:
        wikipedia.set_lang("en")
        result = wikipedia.summary(query, sentences=2)
        speak(engine, f"According to Wikipedia: {result}")

    except wikipedia.exceptions.DisambiguationError as e:
        speak(engine, f"Multiple results found. Please be more specific. For example: {e.options[0]}")

    except wikipedia.exceptions.PageError:
        speak(engine, f"Sorry, I couldn't find any Wikipedia article on {query}.")

    except Exception:
        speak(engine, "Sorry, something went wrong with the Wikipedia search.")


def open_website(engine, site_name):
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://www.github.com",
        "wikipedia": "https://www.wikipedia.org",
    }

    site_name = site_name.lower()
    if site_name in sites:
        speak(engine, f"Opening {site_name}...")
        webbrowser.open(sites[site_name])
    else:
        speak(engine, f"Sorry, I don't have {site_name} in my list. Try: YouTube, Google, GitHub, or Wikipedia.")


def tell_time(engine):
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(engine, f"The current time is {current_time}.")


def tell_date(engine):
    now = datetime.datetime.now()
    current_date = now.strftime("%A, %B %d, %Y")
    speak(engine, f"Today is {current_date}.")


def tell_joke(engine):
    joke = pyjokes.get_joke(language='en', category='all')
    speak(engine, joke)


def take_note(engine, note_text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "my_notes.txt"

    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {note_text}\n")

    speak(engine, f"Note saved: {note_text}")
    print(f"  📝 Note saved to '{filename}'")


def calculate(engine, expression):
    expression = expression.replace("plus", "+")
    expression = expression.replace("minus", "-")
    expression = expression.replace("times", "*")
    expression = expression.replace("multiplied by", "*")
    expression = expression.replace("divided by", "/")
    expression = expression.replace("x", "*")
    expression = expression.replace("into", "*")

    try:
        result = eval(expression)
        speak(engine, f"The answer is {result}.")
    except Exception:
        speak(engine, "Sorry, I couldn't calculate that. Please try again.")


def show_help(engine):
    help_text = (
        "Here are the commands I understand: "
        "Say 'Wikipedia' followed by your search term to search Wikipedia. "
        "Say 'Open' followed by a website name like YouTube or Google. "
        "Say 'Time' to hear the current time. "
        "Say 'Date' to hear today's date. "
        "Say 'Joke' to hear a funny joke. "
        "Say 'Note' followed by your note to save it. "
        "Say 'Calculate' followed by a math expression. "
        "Say 'Help' to hear this list again. "
        "Say 'Exit' or 'Quit' or 'Bye' to stop me."
    )
    speak(engine, help_text)


def run_assistant():

    print("\nVoice Assistant — KKR Gen AI Innovations")


    print("\n  Choose input mode:")
    print("  [1] Voice (requires microphone)")
    print("  [2] Text  (keyboard input)")
    mode = input("\n  Enter 1 or 2: ").strip()
    use_voice = (mode == "1")

    engine = init_engine()
    wish_user(engine)
    speak(engine, "Type 'help' or say help to see what I can do.")

    while True:
        if use_voice:
            query = take_command_voice(engine)
        else:
            query = take_command_text()

        if not query or query == "none":
            continue

        if "wikipedia" in query:
            search_term = query.replace("wikipedia", "").strip()
            if search_term:
                search_wikipedia(engine, search_term)
            else:
                speak(engine, "What should I search on Wikipedia? Please say the topic.")

        elif "open" in query:
            site = query.replace("open", "").strip()
            if site:
                open_website(engine, site)
            else:
                speak(engine, "Which website should I open? Try: open YouTube.")

        elif "time" in query:
            tell_time(engine)

        elif "date" in query:
            tell_date(engine)

        elif "joke" in query:
            tell_joke(engine)

        elif "note" in query:
            note_content = query.replace("note", "").strip()
            if note_content:
                take_note(engine, note_content)
            else:
                speak(engine, "What should I note down? Please say your note after the word 'note'.")

        elif "calculate" in query:
            expression = query.replace("calculate", "").strip()
            if expression:
                calculate(engine, expression)
            else:
                speak(engine, "What should I calculate? For example: calculate 5 plus 3.")

        elif "help" in query:
            show_help(engine)

        elif any(word in query for word in ["exit", "quit", "bye", "goodbye", "stop"]):
            speak(engine, "Goodbye! Have a great day. This is your Gen AI Innovations Voice Assistant signing off.")
            print("\n  👋 Session ended. Thank you for using  Gen AI Innovations Voice Assistant!\n")
            break

        else:
            speak(engine, f"Sorry, I didn't understand '{query}'. Say 'help' to see available commands.")


if __name__ == "__main__":
    run_assistant()