import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM
import PyPDF2
 
torch.cuda.empty_cache()
# creating a pdf file object

pdfFileObj = open(r"D:\PDF\reviewfilm.pdf", 'rb')   # over here we will have to get the name of the filefrom the front end that is the webpage and just put it here
# creating a pdf reader object

pdfReader = PyPDF2.PdfReader(pdfFileObj)

# printing number of pages in pdf file
l = len(pdfReader.pages)
print("no of pages is ",l)
p=''

# creating a page object
for i in range(0,l):
    pageObj = pdfReader.pages[i]
    p += pageObj.extract_text()

# closing the pdf file object
pdfFileObj.close()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    device_map='auto',
    token = "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"
)

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
def get_llama2_reponse(prompt, max_new_tokens=50):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, temperature= 0.000001)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

prompt = p
pr = input("enter your prompt: ")
prompt = prompt + pr

response = get_llama2_reponse(prompt,max_new_tokens=50)

torch.cuda.empty_cache()
print(response)