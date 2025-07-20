from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of France?", temperature=0.7, max_completion_tokens=50)

print(result.content)