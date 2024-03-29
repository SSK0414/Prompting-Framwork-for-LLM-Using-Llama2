import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",
    device_map='auto',
    token = "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"
)

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

inputs = tokenizer("She is", return_tensors="pt").to(device)

print(inputs)

outputs = model.generate(**inputs, max_new_tokens=10)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)