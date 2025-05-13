# 🧠 Smart Voice Assistant using Python

A **smart voice-controlled assistant built with Python** that responds to your spoken commands to open websites or local folders — completely **hands-free**. Ideal for multitaskers, productivity seekers, and Python automation enthusiasts.

---

## 🚀 What This Python Voice Assistant Can Do

Speak commands like:

- 🗣️ `"Open Google"` → opens **google.com**  
- 🗣️ `"Open the Web folder"` → opens a **local folder** on your PC

The assistant listens to your voice, processes the command using **speech recognition**, and performs the appropriate task.

---

## 🎯 Key Features

- 🎤 **Voice Recognition**: Converts spoken input into text  
- 💬 **Text-to-Speech Engine**: Speaks back to you using `pyttsx3`  
- 🌐 **Website Launcher**: Opens URLs from `links.txt` (e.g. Google, YouTube, etc.)  
- 🗂️ **Folder Access**: Opens folders stored in `Local Folders.txt`  
- 🧠 **Fully Offline Speech** (text-to-speech doesn't need internet)  
- 📦 Lightweight and beginner-friendly project for Python learners  

---

## 📂 Folder & File Structure

```plaintext
📦 smart-voice-assistant-python
├── main.py                  # Main Python script for assistant
├── links.txt                # Key-value pairs of site names and URLs
├── Local Folders.txt        # Folder commands and their system paths
└── README.md                # Project documentation
```

---
## 📦 Requirements

Before running the project, make sure you have the following Python libraries installed:

```bash
pip install speechrecognition pyttsx3 pyaudio
```
| Library             | Purpose                                                              |
| ------------------- | -------------------------------------------------------------------- |
| `speechrecognition` | Captures audio and converts your **voice into text**                 |
| `pyttsx3`           | Converts **text into speech** so the assistant can talk back to you  |
| `pyaudio`           | Handles **microphone input** and audio streaming (backend for input) |

---
## ⚙️ How It Works

This Smart Voice Assistant listens to your voice, understands your command, and performs actions such as opening websites or folders — all hands-free!

### 🔄 Step-by-Step Workflow:

1. **Startup Greeting**  
   The assistant greets you with a friendly message using text-to-speech (TTS).

2. **Voice Listening**  
   It listens through your microphone and waits for your command (e.g., “Open Google”, “Open the Web folder”).

3. **Speech Recognition**  
   It converts your voice into text using Google’s Speech Recognition API.

4. **Command Matching**  
   The assistant searches your command against:
   - `links.txt` → for website names and URLs
   - `Local Folders.txt` → for folder names and paths

5. **Action Execution**  
   If a match is found:
   - 🌐 Opens the website in your default browser  
   - 📂 Opens the local folder using your file explorer  
   - 🔊 Speaks back the action being taken

6. **Error Handling**  
   If the command is not recognized or understood, the assistant responds with an error message.


This flow ensures a smooth, fast, and interactive voice-controlled experience — great for productivity and accessibility!

## 📥 Clone This Repository

To get a copy of this project on your local machine, run the following command in your terminal:

```bash
git clone https://github.com/Tirth9978/smart-voice-assistant-python.git
```
---

> 📝 **Note:** You can customize the `links.txt` and `Local Folders.txt` files to add your own websites and folders as per your convenience.
> 💡 **Tip:** Feel free to update the contents of `links.txt` and `Local Folders.txt` to include the websites and local folders you use most often. This makes the assistant truly personalized to your workflow!


## 🤝 Contributing

Contributions are welcome and appreciated! Whether it's improving the code, fixing bugs, adding new features, or enhancing documentation — every bit helps.

### 🧾 How to Contribute

1. Fork the repository  
2. Create a new branch  
   ```bash
   git checkout -b feature/your-feature-name
   ```

### 📌 Contribution Guidelines

- ✅ Follow clean code practices  
- 🔍 Keep your pull requests focused and minimal  
- 📝 Add comments and documentation where helpful  
- 🧪 Test your code thoroughly before submitting  

>💬 If you're not sure where to start, check the open issues or feel free to open a discussion.

## 👤 Author

| 🧑‍💻 Name     | Tirth Patel                           |
|--------------|----------------------------------------|
| 🔗 GitHub    | [@Tirth9978](https://github.com/Tirth9978) |
| 💼 About Me | Passionate Python developer focused on building productivity tools, automation scripts, and accessible tech using AI and voice technology. Always learning and exploring new ways to solve real-world problems with code. |

> If you found this project helpful or inspiring, feel free to ⭐ star the repo and follow me on GitHub for more cool projects!

