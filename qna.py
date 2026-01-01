from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

print("Enter context (end with an empty line):")
lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)

context = " ".join(lines)

question = input("Enter your question: ")

result = qa_pipeline({
    "context": context,
    "question": question
})

print("\nAnswer:", result["answer"])
print("Confidence:", round(result["score"], 2))
