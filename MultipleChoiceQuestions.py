from transformers import pipeline
import pdfplumber

def read_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

text = read_pdf("document.pdf")

generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-1.5B-Instruct",
    device_map="auto"
)

prompt = f"""
Create 5 multiple-choice questions from the following text.

For each question provide:
Question:
A)
B)
C)
D)
Answer:

Text:
{text[:3000]}
"""

result = generator(
    prompt,
    max_new_tokens=800,
    do_sample=False
)

print(result[0]["generated_text"])
