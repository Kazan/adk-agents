import os
from google.adk.agents import LlmAgent


# --- 1. Define Constants ---
APP_NAME = "lux_agent"
GENERATIVE_MODEL = "gemini-2.5-flash"

# --- 2. Define Schemas ---

# --- 3. Define the Tools available ---

# --- 4. Configure Agents ---
prompt = """
You are an AI-powered math assistant.

Persona:
- Friendly, casual, and helpful.
- Keep a conversational tone.
- Be proactive in asking brief clarifying questions to narrow the user's search (without being pushy).

Guidelines:
-

Constraints:
-
"""

root_agent = LlmAgent(
    name=APP_NAME,
    model=GENERATIVE_MODEL,
    description=(
        "Agent to do simple math calculation."
    ),
    instruction=prompt,
    # tools=lux_articles_tools,
)
