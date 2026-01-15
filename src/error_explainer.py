import os
from google import genai
from dotenv import load_dotenv
from prompt_template import generate_prompt

# --------------------------
# 1️⃣ Load API key and init client
# --------------------------
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise Exception("Set GOOGLE_API_KEY in your .env file")

# Initialize the modern Client
client = genai.Client(api_key=API_KEY)

# --------------------------
# 2️⃣ Execution Functions
# --------------------------

def run_code_and_capture_error(code):
    """
    Runs code and captures the exception message.
    Returns None if no error occurs.
    """
    try:
        # Using a shared dict for globals/locals to mimic a real environment
        exec_globals = {}
        exec(code, exec_globals)
        return None
    except Exception as e:
        return str(e)


def explain_error_with_llm(code):
    """
    Sends the code + captured error to Gemini and gets an explanation.
    """
    error_message = run_code_and_capture_error(code)
    
    if not error_message:
        return "No error found in code."

    # This uses your existing prompt_template.py logic
    prompt = generate_prompt(code, error_message)

    # ---------------------------------------
    # 3️⃣ Call Gemini (Modern SDK Syntax)
    # ---------------------------------------
    # Note: 'gemini-2.5-flash' is the standard current identifier.
    print(prompt)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "temperature": 0.2,
            "max_output_tokens": 1999,
        }
    )

    return response.text

# --------------------------
# 4️⃣ Sanity Check
# --------------------------
if __name__ == "__main__":
    test_code = 'x = 10\nprint(y)'
    print("--- Running Error Explainer ---")
    explanation = explain_error_with_llm(test_code)
    print(explanation)