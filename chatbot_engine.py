import os
import spacy
import fitz  # PyMuPDF
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

# ----------- Helper: Clean text for PDF decoding
def clean_text(text):
    return text.replace("—", "-").replace("’", "'").replace("“", "\"").replace("”", "\"")

# ----------- Preprocessing
def preprocess(text):
    doc = nlp(text.lower())
    return " ".join(token.lemma_ for token in doc if token.is_alpha and not token.is_stop)

# ----------- Extract Q&A from PDF
def extract_faq_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    lines = text.split('\n')

    faq_pairs = []
    current_q, current_a = None, None

    for line in lines:
        line = clean_text(line.strip())
        if line.startswith('Q') and ':' in line:
            if current_q and current_a:
                faq_pairs.append({'question': current_q, 'answer': current_a})
                current_q, current_a = None, None
            current_q = line.split(':', 1)[1].strip()
        elif line.startswith('A') and ':' in line:
            current_a = line.split(':', 1)[1].strip()
        elif current_a is not None:
            current_a += ' ' + line

    if current_q and current_a:
        faq_pairs.append({'question': current_q, 'answer': current_a})

    return pd.DataFrame(faq_pairs)

# ----------- Initialize
faq_pdf_path = os.path.join("data", "chatgpt_detailed_faq.pdf")
faq_df = extract_faq_from_pdf(faq_pdf_path)
faq_df["processed_question"] = faq_df["question"].apply(preprocess)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(faq_df["processed_question"])

# ----------- Matching Engine
def get_best_answer(user_question):
    processed_input = preprocess(user_question)
    input_vec = vectorizer.transform([processed_input])
    similarities = cosine_similarity(input_vec, X)
    best_idx = similarities.argmax()
    best_score = similarities[0][best_idx]

    if best_score > 0.4:
        return faq_df.iloc[best_idx]["answer"]
    else:
        return "Sorry, I couldn't find a matching answer. Please try rephrasing."
