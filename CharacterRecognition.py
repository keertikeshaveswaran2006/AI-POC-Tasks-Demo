from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image
import os

model_name = "Qwen/Qwen2.5-VL-3B-Instruct"

processor = AutoProcessor.from_pretrained(model_name)
model = AutoModelForImageTextToText.from_pretrained(model_name)

print("Current working directory:", os.getcwd())
print("Script location:", os.path.dirname(os.path.abspath(__file__)))

image = Image.open("document.png")

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": "Extract all text from this image exactly as written."}
        ]
    }
]

inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    return_tensors="pt",
    return_dict=True
)

outputs = model.generate(**inputs, max_new_tokens=1000)

result = processor.decode(outputs[0], skip_special_tokens=True)
print(result)
