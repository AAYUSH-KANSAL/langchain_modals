from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=1536)

result = embeddings.embed_query("Delhi is the capital of India")

print(str(result))  # Output the embeddings as a string
# Note: The output will be a list of floats representing the embeddings.