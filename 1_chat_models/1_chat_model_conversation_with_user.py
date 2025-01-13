from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage , HumanMessage , SystemMessage

# Load Environment Veriable form .env 
load_dotenv()

model = ChatOpenAI(model = 'gpt-4o-mini')

# storing conversation in local storage 
chat_history = []

# set an initial system message 
system_message = SystemMessage(content= 'you are a helpful AI Assistant')
chat_history.append(system_message)


# Chat loop 
while True : 
    Query = input("you : ")
    if Query.lower()=='exit':
        break

    chat_history.append(HumanMessage(content=Query))
    result = model.invoke(Query)
    chat_history.append(AIMessage(content=result.content))

    print('AI : ' , result.content)

print("---Message History---")
print(chat_history)




