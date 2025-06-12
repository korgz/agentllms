import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
print("Anthropic API key loaded:", bool(api_key))

if not api_key:
    print("Error: ANTHROPIC_API_KEY not found in environment variables.")
    exit(1)

llm = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    anthropic_api_key=api_key
)

prompt = "Say hello!"

try:
    response = llm.invoke([HumanMessage(content=prompt)])
    print("Response from Anthropic:")
    print(response.content)
except Exception as e:
    print("Error while calling Anthropic API:", e)
