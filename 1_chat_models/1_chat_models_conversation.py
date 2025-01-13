# types of messages 

# - system message 
# - human message 
# - AI message

# ChatModels take a list of messages as input and return a message. There are a few different types of messages. All messages have a role and a content property. The role describes WHO is saying the message. LangChain has different message classes for different roles. The content property describes the content of the message. This can be a few different things:

# A string (most models deal this type of content)
# A List of dictionaries (this is used for multi-modal input, where the dictionary contains information about that input type and that input location)
# In addition, messages have an additional_kwargs property. This is where additional information about messages can be passed. This is largely used for input parameters that are provider specific and not general. The best known example of this is function_call from OpenAI.

# HumanMessage
# This represents a message from the user. Generally consists only of content.

# AIMessage
# This represents a message from the model. This may have additional_kwargs in it - for example tool_calls if using OpenAI tool calling.

# SystemMessage
# This represents a system message, which tells the model how to behave. This generally only consists of content. Not every model supports this.

# FunctionMessage
# This represents the result of a function call. In addition to role and content, this message has a name parameter which conveys the name of the function that was called to produce this result.

# ToolMessage
# This represents the result of a tool call. This is distinct from a FunctionMessage in order to match OpenAI's function and tool message types. In addition to role and content, this message has a tool_call_id parameter which conveys the id of the call to the tool that was called to produce this result.

 

from langchain_core.messages import SystemMessage , HumanMessage , AIMessage 
from langchain_openai import ChatOpenAI


llm = ChatOpenAI (model = "gpt-4o-mini")

message = [
    SystemMessage('you are an expert in social media content strategy'),
    HumanMessage('Give a short tip to create engaging post on instagram' ),
    AIMessage('Use high-quality visuals paired with a captivating caption. Start with a hook in your caption to grab attention, ask a question to encourage interaction, and always include relevant hashtags to increase discoverability. Engage with your audience by responding to comments and using Instagram Stories to share behind-the-scenes content or polls to foster community.'),
    HumanMessage('give more tips')
]

result = llm.invoke(message)
print(result.content)