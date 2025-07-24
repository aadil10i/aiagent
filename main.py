import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info

if len(sys.argv) < 2:
    print("error no input provided")
    sys.exit(1)

# list of available functions in functions/
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_input = sys.argv[1]
messages = [types.Content(role="user", parts=[types.Part(text=user_input)])]

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    ),
)

has_function_call = False
if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
    for part in response.candidates[0].content.parts:
        if part.function_call:
            has_function_call = True
            fc = part.function_call
            args = {key: val for key, val in fc.args.items()}
            print(f"Calling function: {fc.name}({args})")

if not has_function_call:
    print(response.text)

p_token = response.usage_metadata.prompt_token_count
r_token = response.usage_metadata.candidates_token_count

print(f"\nPrompt Tokens: {p_token} \nResponse Tokens: {r_token}")
