from google.adk.agents import LlmAgent
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

Constraints:
-
"""

# --- 5. Configure Agent ---
toolset.get_tools()

root_agent = LlmAgent(
    name=APP_NAME,
    model=GENERATIVE_MODEL,
    description=(
        "Agent to do simple math calculation."
    ),
    instruction=prompt,
    tools=[toolset]
)
