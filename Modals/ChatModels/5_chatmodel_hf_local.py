from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline

import os
os.environ['HF_HOME'] = 'E:/HUGGINGFACE'

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.7,
        "max_new_tokens": 50
    } 
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("virat kholi vs ms dhoni?", temperature=0.7, max_completion_tokens=50)
print(result.content)
