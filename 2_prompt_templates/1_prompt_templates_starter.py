from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model = 'gpt-4o-mini')

template = 'write a {tone} email to {company} asking for LOR for masters in US'

prompt_template = ChatPromptTemplate.from_template(template=template)

# here invoke will change the placeholders with real values
prompt = prompt_template.invoke({'tone' : 'formal' , 'company' : 'Broader AI'})

# here invoke will call llm 
result = llm.invoke(prompt)
print(result.content)
