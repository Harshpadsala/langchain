# using chain method to chain up the invokes in seq
# docs : https://python.langchain.com/docs/how_to/sequence/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda , RunnableSequence
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatOpenAI(model = 'gpt-4o-mini')

# Define prompt templates )no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages([
    ('system' , 'you are a facts expert who knows facts about {animal}'),
    ('human','tell me {fact_count} facts')
])

format_prompt = RunnableLambda(lambda x : prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x : model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x : x.content)

chain = RunnableSequence(first=format_prompt , middle=[invoke_model],last=parse_output)
result = chain.invoke({'animal':'cat','fact_count':3})
print(result)



