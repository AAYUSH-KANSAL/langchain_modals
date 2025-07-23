from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenAI(model="gemini-1.5-pro")
result = model.invoke("What is the capital of France?", temperature=0.7, max_completion_tokens=50)

print(result.content)
