from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch
from langchain.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model = 'gpt-4o-mini')

# Run the chain with an example review
# Good review - "The product is excellent. I really enjoyed using it and found it very helpful."
# Bad review - "The product is terrible. It broke after just one use and the quality is very poor."
# Neutral review - "The product is okay. It works as expected but nothing exceptional."
# Default - "I'm not sure about the product yet. Can you tell me more about its features and benefits?


classification_template = ChatPromptTemplate.from_messages(
    [
        ('system' , 'you are a helpful assistant'),
        ('human' , 'classify the sentiment of this feedback as positive , negative , neutral or escalate : {feedback}')
    ]
)

# Define prompt templates for different feedback types
positive_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human",
         "Generate a thank you note for this positive feedback: {feedback}."),
    ]
)

negative_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human",
         "Generate a response addressing this negative feedback: {feedback}."),
    ]
)

neutral_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Generate a request for more details for this neutral feedback: {feedback}.",
        ),
    ]
)

escalate_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Generate a message to escalate this feedback to a human agent: {feedback}.",
        ),
    ]
)

# Define the runnable branches for handling feedback
branches = RunnableBranch(
    (
        lambda x : 'positive' in x,
        positive_feedback_template | model | StrOutputParser()
    ),
    (
        lambda x : 'negative' in x,
        negative_feedback_template | model | StrOutputParser()
    ),
    (
        lambda x : 'neutral' in x,
        neutral_feedback_template | model | StrOutputParser()
    ),
    escalate_feedback_template | model | StrOutputParser()

)

classification_chain = classification_template | model | StrOutputParser()

chain = classification_chain | branches 

review = 'The product is excellent. I really enjoyed using it and found it very helpful.'

result = chain.invoke({"feedback" : review})
print(result)