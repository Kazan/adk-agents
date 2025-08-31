from google.adk.agents import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent, AGENT_CARD_WELL_KNOWN_PATH
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

# --- 1. Define Constants ---
APP_NAME = "CalculatingAgent"
GENERATIVE_MODEL = "gemini-2.5-flash"

# --- 2. Define Schemas ---
#  N/A

# --- 3. Define the Tools available ---
toolset = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="http://localhost:8080",
    ),
)

# --- 4. Configure Prompt ---
prompt = """
You are an AI-powered math assistant.

Persona:
- Friendly, casual, and helpful.
- Keep a conversational tone.
- Be proactive in asking brief clarifying questions to narrow the user's search (without being pushy).

Guidelines:
- You will always reply to math specific questions in json format, with the following structure:
```json
{
    "question": "<user's question>",
    "answer": "<just the resulting number>"
}
```
- Use the calculate tool to perform the arithmetic operations if there are any
- if the user asks whether the result is even or odd, delegate the task to the "evenodd_agent"

Constraints:
- Do not reply to absolutely anything which is not a math calculation.
"""

# --- 5. Configure Agents ---
evenodd_agent = RemoteA2aAgent(
    name="evenodd_agent",
    description="Agent that handles checking if numbers are even or odd.",
    agent_card=(
        f"http://localhost:8001/a2a/even_odd{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

calc_agent = Agent(
    name=APP_NAME,
    model=GENERATIVE_MODEL,
    description=(
        "Agent to do simple math calculation."
    ),
    sub_agents=[evenodd_agent],
    instruction=prompt,
    tools=[toolset],
    before_model_callback=None
)

root_agent = calc_agent
