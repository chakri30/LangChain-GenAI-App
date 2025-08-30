import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Import the necessary classes
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate

# Instantiate your LLM (using the Google model with your API key)
# The library will automatically find the GOOGLE_API_KEY environment variable.
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash") 

# Step 1: Create a memory object
memory = ConversationBufferMemory()

# Step 2: Create a prompt template that includes a variable for chat history
# The 'history' variable is crucial for the memory to work
template = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context.

Current conversation:
{history}
Human: {input}
AI:"""
prompt = PromptTemplate(input_variables=["history", "input"], template=template)

# Step 3: Create the Conversation Chain and link the memory to it
# The ConversationChain handles the logic of injecting the chat history into the prompt
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True # Set this to True to see the full prompts being sent to the LLM
)

# Step 4: Run the conversation in multiple turns
print(conversation.invoke({"input": "What is the capital of France?"}))

print(conversation.invoke({"input": "What is the primary language spoken there?"}))

print(conversation.invoke({"input": "What else do you know about that city?"}))

# To see the full history in the memory object
print("\n--- Full Conversation History ---")
print(memory.load_memory_variables({}))