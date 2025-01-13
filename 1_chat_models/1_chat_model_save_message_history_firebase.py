# firebase project id : langchain-123
from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI

load_dotenv()

PROJECT_ID = 'langchain-123'
SESSION_ID = "user_session_new"
COLLECTION_NAME = 'chat_history'

# Initialize FireStore Client
print("Initializing firestore client")
client = firestore.Client(project= PROJECT_ID)

# Initialization FireStore Chat Message History 
print('Initializing Firestore Chat Message History')

chat_history = FirestoreChatMessageHistory(session_id=SESSION_ID , collection= COLLECTION_NAME , client= client)

print("Chat History Initialized")
print("Current Chat History:" , chat_history.messages)

model = ChatOpenAI(model = 'gpt-4o-mini')

print("Starting chatting with AI,  type 'exit' to quit ")

while True:
    human_msg = input('User : ')
    if human_msg.lower() == 'quit':
        break

    chat_history.add_user_message(human_msg)

    AI_response =  model.invoke(human_msg)
    chat_history.add_ai_message(AI_response.content)
    print("AI : ", AI_response.content)


print()
print("______________________ALL MESSAGES_______________________")
print(chat_history.aget_messages())


