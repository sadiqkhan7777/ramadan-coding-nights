import os
import requests
import chainlit as cl
from agents import Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv
from agents.tool import function_tool
from typing import Optional, Dict

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)

config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True,
)


@function_tool("get_sadiq_data")
def get_sadiq_data() -> str:
    """
    Fetches profile data about Sadiq khan from his personal API endpoint.

    This function makes a request to Asharib's profile API and returns information
    about his background, skills, projects, education, work experience, and achievements.

    Returns:
        str: JSON string containing Asharib Ali's profile information
    """

    try:
        response = requests.get("https://www.asharib.xyz/api/profile")
        if response.status_code == 200:
            return response.text
        else:
            return f"Error fetching data: Status code {response.status_code}"
    except Exception as e:
        return f"Error fetching data: {str(e)}"


agent = Agent(
    name="Greeting Agent",
    instructions="""You are a Greeting Agent designed to provide friendly interactions and information about Sadiq khan.

Your responsibilities:
1. Greet users warmly when they say hello (respond with 'Salam from Sadiq khan')
2. Say goodbye appropriately when users leave (respond with 'Allah Hafiz from Sadiq khan')
3. When users request information about Sadiq khan, use the get_sadiq_data tool to retrieve and share his profile information
4. For any questions not related to greetings or Sadiq khan, politely explain: 'I'm only able to provide greetings and information about Sadiq khan. I can't answer other questions at this time.'

Always maintain a friendly, professional tone and ensure responses are helpful within your defined scope.""",
    model=model,
    tools=[get_sadiq_data],
)


@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:
    """
    Handle the OAuth callback from GitHub
    Return the user object if authentication is successful, None otherwise
    """
    print(f"Provider: {provider_id}")
    print(f"User data: {raw_user_data}")

    return default_user


@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])

    await cl.Message(
        content="Hello, how can I help you today?"
    ).send()


@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history", [])

    history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")
    await msg.send()

    result = Runner.run_streamed(
        agent,
        input=history,
        run_config=config,
    )

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            await msg.stream_token(event.data.delta)

    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)