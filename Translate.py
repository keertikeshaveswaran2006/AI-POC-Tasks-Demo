#MODULES
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

#FILES
f=open('Frenchtext.txt','r')
text=f.read()

#API DEPENDENCIES
model_name = "Helsinki-NLP/opus-mt-fr-en"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

#MAIN
inputs = tokenizer(text, return_tensors="pt")
outputs = model.generate(**inputs)

translated = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(translated)
