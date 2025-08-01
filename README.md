# 🤖 ChatGPT FAQ Chatbot

A lightweight, NLP-powered FAQ chatbot that extracts questions and answers from a PDF file (no need for CSV or JSON!), preprocesses the content using spaCy, and matches user queries using cosine similarity over TF-IDF vectors — all wrapped in a simple Flask web app.

---

## 🧠 Features

- ✅ **PDF-based FAQ ingestion** (reads directly from a `.pdf` file)
- 🧼 **NLP Preprocessing** with spaCy (lemmatization, stopword removal)
- 🔍 **TF-IDF + Cosine Similarity** for matching questions
- 💬 **Flask UI** with user-friendly input/output
- 🧱 Modular design — easy to extend with semantic search or feedback logging

---

## 🗂 Project Structure


faq_chatbot_flask/
├── app.py # Flask app entrypoint
├── chatbot_engine.py # PDF extractor + NLP matcher
├── data/
│ └── chatgpt_detailed_faq.pdf # FAQ content source
├── static/
│ └── style.css # Optional styling for UI
├── templates/
│ └── index.html # HTML form UI
├── requirements.txt # Python dependencies
└── README.md # You're here!

yaml

---

## 🚀 Getting Started

### 1. Set up the Python Environment

We recommend using `pyenv` + `pyenv-virtualenv`:

```bash
pyenv install 3.10.13
pyenv virtualenv 3.10.13 faq-chatbot-env
pyenv activate faq-chatbot-env
```
### 2. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Run the Flask App

```bash
python app.py
```
Visit http://localhost:5000 in your browser.

---

## 💬 Sample Questions

Try asking:

- "What is ChatGPT?"
- "Can it write code?"
- "Does ChatGPT support international languages?"
- "How do I reset my password?" ← (if your own FAQ includes it)

---

## 🛠️ Customization Ideas

- Use **Sentence-BERT** or **OpenAI embeddings** for semantic matching
- Log **unanswered questions** for feedback-driven improvement
- **Dockerize** the app for easier deployment
- Add **session-based chat history**

---

## 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
