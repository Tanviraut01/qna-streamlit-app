## Project Structure
# Question Answering Web App (Transformers)

## Overview
This project is a Question Answering (QnA) web application built using a pre-trained Transformer model. Users provide a text passage (context) and ask a question. The system extracts the most relevant answer from the context and displays it along with a confidence score.

## Objective
- Build a QnA system using a pre-trained NLP model
- Accept user input (context + question)
- Display accurate answers with confidence
- Provide a simple, interactive web interface
- Deploy the application online

## Tech Stack
- Python
- Hugging Face Transformers
- PyTorch
- Streamlit
- GitHub

## Project Structure
- app.py
- qna.py
- requirements.txt

## Implementation Steps
1. **Model Selection:** Used a pre-trained DistilBERT model fine-tuned on SQuAD for question answering.
2. **Pipeline Integration:** Implemented Hugging Face `pipeline("question-answering")` to simplify inference.
3. **Input Handling:** Collected context and question from the user.
4. **Inference:** Passed inputs to the model to extract the answer and confidence score.
5. **Web Interface:** Built an interactive UI using Streamlit.
6. **Customization:** Added gradient background and styled inputs/buttons using CSS.
7. **Deployment:** Hosted the app using GitHub and Streamlit Community Cloud.

## How It Works
1. User enters a context paragraph.
2. User types a question related to the context.
3. The Transformer model analyzes the text.
4. The most relevant answer is extracted.
5. The answer and confidence score are displayed.

## Local Setup
cmd:-
pip install -r requirements.txt
streamlit run app.py
