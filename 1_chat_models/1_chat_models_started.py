from langchain_openai import ChatOpenAI
import os 

openai_api = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI (model = "gpt-4o-mini")

result = llm.invoke('explain about virat kohli in 50 words')
print(result.content) 