from langchain_core.messages import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # Replace ChatOpenAI
from langchain.chat_models import ChatOpenAI

#load the environment variables from the .env file
load_dotenv()

openAI_key = os.getenv("OPENAI_API_KEY")
if not openAI_key:
    print("OPENAI_API_KEY is missing from .env file. Please set it.")
    exit(1)  # or raise an error indicating the API key is missing

print(f"Successfully loaded OpenAI API key: {openAI_key}")

llm_name = "gpt-4o"

model = ChatOpenAI(
    api_key=openAI_key,
    model = "gpt-4o",
    temperature=0)

# messages = [ 
#     SystemMessage(content="You are a helpful assistant who is extremely competent, as a Computer Scientist! Your name is Chint."),
#     HumanMessage(content="Who was the very first computer scientist?")
# ]

messages = [
    {"role": "system", "content": "You are a helpful assistant who is extremely competent, as a Computer Scientist! Your name is Chint."},
    {"role": "user", "content": "Who was the very first IT company of the world?"}
]

# try:
#     response = model.invoke(messages)
#     print("Response content:", response.content)
# except Exception as e:
#     print(f"Error: {e}")

def first_agent(messages):
    response = model.invoke(messages)
    return response


def run_agent():
    print("Simple AI Agent: Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print("AI Agent is thinking...")
        messages = [HumanMessage(content=user_input)]
        response = first_agent(messages)
        print("AI Agent: getting the response...")
        print(f"AI Agent: {response.content}")

if __name__ == "__main__":
    run_agent()

