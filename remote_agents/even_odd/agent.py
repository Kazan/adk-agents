from google.adk.agents import Agent

# --- 1. Define Constants ---
APP_NAME = "EvenOddAgent"
GENERATIVE_MODEL = "gemini-2.5-flash"


# --- 4. Configure Prompt ---
prompt = """
You are an agent which sole purpose is to determine if a given number is even or odd.
You will not reply or engage in any other type of conversation.
You will always reply with the following json format:
```json
{
    "question": "<user's question>",
    "value": <user's number>,
    "is_even": <boolean value>
}
```
"""

root_agent = Agent(
    name=APP_NAME,
    model=GENERATIVE_MODEL,
    description=(
        "Agent to determine if a number even or odd"
    ),
    instruction=prompt,
)
