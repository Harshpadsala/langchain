from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage ,  SystemMessage

# Langchain chat models doc : 
# https://python.langchain.com/v0.1/docs/modules/model_io/chat/

load_dotenv()

messages = [
    SystemMessage('you are an expert in mathematics'),
    HumanMessage('what is value of -1/12')
]

# openai_chat model 

model = ChatOpenAI(model = 'gpt-4o-mini')

result = model.invoke(messages)
print("Result form open ai :" , result.content)
print()


# chat anthropic model
# 
# we need paid anthropic api key
#  
# model = ChatAnthropic(model = 'claude-3-5-sonnet-20241022')

# result = model.invoke(messages)
# print("Result form anthropic :" , result.content)
# print()


# gemini model 
model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash')

result = model.invoke(messages)
print("Result form gemini  :" , result.content)
print()

