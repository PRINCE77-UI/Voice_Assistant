# Sample Output Examples — Voice Assistant using Python

> These examples show exactly what you will see in the terminal when you run `voice_assistant.py`.

---

## Startup Screen

```
   Voice Assistant —  Gen AI Innovations

  Choose input mode:
  [1] Voice (requires microphone)
  [2] Text  (keyboard input)

  Enter 1 or 2: 2
```

---

## Example 1 — Greeting (Morning)

```
  🤖 Assistant: Good Morning! I am your Voice Assistant, powered by  Gen AI
               Innovations. How can I help you today?

  🤖 Assistant: Type 'help' or say help to see what I can do.
```

---

## Example 2 — Wikipedia Search

```
  ⌨️  You (type command): wikipedia artificial intelligence

  🤖 Assistant: Searching Wikipedia for artificial intelligence...

  🤖 Assistant: According to Wikipedia: Artificial intelligence (AI) is
               intelligence demonstrated by machines, as opposed to the
               natural intelligence displayed by animals including humans.
               AI research has been defined as the field of study of
               intelligent agents, which refers to any system that perceives
               its environment and takes actions that maximize its chance of
               achieving its goals.
```

---

## Example 3 — Current Time

```
  ⌨️  You (type command): time

  🤖 Assistant: The current time is 02:50 PM.
```

---

## Example 4 — Today's Date

```
  ⌨️  You (type command): date

  🤖 Assistant: Today is Saturday, Oct 3, 2026.
```

---

## Example 5 — Open a Website

```
  ⌨️  You (type command): open youtube

  🤖 Assistant: Opening youtube...
  [YouTube opens in your default web browser]
```

---

## Example 6 — Tell a Joke

```
  ⌨️  You (type command): joke

  🤖 Assistant: Why do Java developers wear glasses?
               Because they don't C#!
```

---

## Example 7 — Take a Note

```
  ⌨️  You (type command): note buy groceries after college today

  🤖 Assistant: Note saved: buy groceries after college today
  📝 Note saved to 'my_notes.txt'
```

**Contents of `my_notes.txt` after the above command:**
```
[2026-03-23 10:38:45] buy groceries after college today
```

---

## Example 8 — Calculator

```
  ⌨️  You (type command): calculate 25 plus 75

  🤖 Assistant: The answer is 100.
```

```
  ⌨️  You (type command): calculate 120 divided by 4

  🤖 Assistant: The answer is 30.0.
```

```
  ⌨️  You (type command): calculate 5 times 6

  🤖 Assistant: The answer is 30.
```

---

## Example 9 — Help Command

```
  ⌨️  You (type command): help

  🤖 Assistant: Here are the commands I understand:
               Say 'Wikipedia' followed by your search term to search Wikipedia.
               Say 'Open' followed by a website name like YouTube or Google.
               Say 'Time' to hear the current time.
               Say 'Date' to hear today's date.
               Say 'Joke' to hear a funny joke.
               Say 'Note' followed by your note to save it.
               Say 'Calculate' followed by a math expression.
               Say 'Help' to hear this list again.
               Say 'Exit' or 'Quit' or 'Bye' to stop me.
```

---

## Example 10 — Unrecognized Command

```
  ⌨️  You (type command): play music

  🤖 Assistant: Sorry, I didn't understand 'play music'.
               Say 'help' to see available commands.
```

---

## Example 11 — Voice Mode (with microphone)

```
  Enter 1 or 2: 1

  🤖 Assistant: Good Afternoon! I am your Voice Assistant...

  🎤 Listening... (speak now)
  ⏳ Recognizing speech...
  🗣️  You said: what is machine learning

  🤖 Assistant: Searching Wikipedia for what is machine learning...

  🤖 Assistant: According to Wikipedia: Machine learning (ML) is a branch of
               artificial intelligence (AI) and computer science that focuses
               on the use of data and algorithms to imitate the way that
               humans learn, gradually improving its accuracy.
```

---

## Example 12 — Exit

```
  ⌨️  You (type command): bye

  🤖 Assistant: Goodbye! Have a great day. This is your  Gen AI Innovations
               Voice Assistant signing off.

  👋 Session ended. Thank you for using Gen AI Innovations Voice Assistant!
```

---

## Summary of All Commands

| Command               | Example Input                        | What Happens                             |
|-----------------------|--------------------------------------|------------------------------------------|
| `wikipedia <topic>`   | `wikipedia python programming`       | Searches and reads Wikipedia summary     |
| `open <site>`         | `open youtube`                       | Opens site in browser                    |
| `time`                | `time`                               | Reads current time                       |
| `date`                | `date`                               | Reads today's date                       |
| `joke`                | `joke`                               | Tells a random joke                      |
| `note <text>`         | `note study AI tonight`              | Saves note to my_notes.txt               |
| `calculate <expr>`    | `calculate 10 times 5`               | Computes and reads the result            |
| `help`                | `help`                               | Lists all commands                       |
| `exit` / `bye`        | `bye`                                | Gracefully shuts down the assistant      |
