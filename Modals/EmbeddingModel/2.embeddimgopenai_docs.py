from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=1536)

documents = [
    "Delhi is the capital of India",
    "Paris is the capital of France",
    "Berlin is the capital of Germany"
]

result = embeddings.embed_documents(documents)

print(str(result))  # Output the embeddings as a string
# Note: The output will be a list of floats representing the embeddings.