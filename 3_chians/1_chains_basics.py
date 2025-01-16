# using chain method to chain up the invokes in seq
# docs : https://python.langchain.com/docs/how_to/sequence/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatOpenAI(model = 'gpt-4o-mini')

# Define prompt templates )no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages([
    ('system' , 'you are a facts expert who knows facts about {animal}'),
    ('human','tell me {fact_count} facts')
])

# create the combined chain using langchain expression language (LCEL)
chain = prompt_template | model | StrOutputParser()

# Run the chain
result = chain.invoke({'animal' : 'dog' , 'fact_count' : 3})
print(result)
