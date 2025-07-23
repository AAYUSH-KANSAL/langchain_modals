from langchain_huggingface import HuggingFaceEmbeddings

import os
os.environ['HF_HOME'] = 'E:/HUGGINGFACE_EMBEDDINGS'


embeddings = HuggingFaceEmbeddings( model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India",    
    "Paris is the capital of France",
    "Berlin is the capital of Germany"
]

vector = embeddings.embed_documents(documents)

print(str(vector))  # Output the embeddings as a string
