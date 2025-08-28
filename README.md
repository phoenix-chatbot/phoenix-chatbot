# Phoenix Chatbot

![Phoenix Logo](A_digital_vector_illustration_of_a_phoenix_emblem_.png)

A local and web-based chatbot powered by Python, OpenAI, speech recognition, and text-to-speech, capable of chatting, riddles, and voice interaction.

---

## 🚀 Features

- 🤖 Chat and riddles interaction
- 🎙️ Voice input with `SpeechRecognition`
- 🔊 Text-to-speech with `pyttsx3`
- 🌐 Streamlit web app interface
- 📦 Packaged into executable using PyInstaller

---

## 🧰 Requirements
Install with pip:

```bash
pip install -r requirements.txt
```

Ensure `PyAudio` and `SpeechRecognition` are installed correctly for voice features.

---

## 🖥️ Running the App

### 💬 Local Chatbot (CLI)
```bash
python chatbot.py
```

### 🌐 Web Interface
```bash
streamlit run app.py
```

---

## 💡 Project Structure
```
phoenix-chatbot/
├── app.py                   # Streamlit web app
├── chatbot.py               # Main CLI chatbot logic
├── requirements.txt         # Python dependencies
├── A_digital_vector_illustration_of_a_phoenix_emblem_.png # Logo
├── README.md                # Project documentation
```

---

## 📦 Packaging to Executable

```bash
pyinstaller --onefile --icon=phoenix.ico chatbot.py
```
> Make sure the `.ico` file exists in the same directory.

---

## 🌍 Deployment Options

- Localhost via Streamlit
- Future idea: Host on **Streamlit Community Cloud** (requires GitHub repo)

---

## 🧠 Credits
- Built by **Phoenix (Idris Olawale)**
- Inspired by creative AI + Python chatbot ideas

---

## 📜 License
MIT License (add license file if needed)

---

> For questions, contact me at `olawalefasasi11@gmail.com`

🔥 Built to riddle, vibe, and talk!
