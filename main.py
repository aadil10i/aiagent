import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

if len(sys.argv) < 2:
    print("error no input provided")
    sys.exit(1)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_input = sys.argv[1]
messages = [types.Content(role="user", parts=[types.Part(text=user_input)])]

system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

p_token = response.usage_metadata.prompt_token_count
r_token = response.usage_metadata.candidates_token_count

print(f"{response.text} \n Prompt Tokens: {p_token} \n Response Tokens: {r_token}")
