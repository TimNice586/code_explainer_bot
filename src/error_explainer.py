import os
from google import genai
from dotenv import load_dotenv
from prompt_template import generate_prompt

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def run_code_and_capture_error(code):
    try:
        exec_globals = {}
        compile(code, "<student_code>", "exec")
        exec(code, exec_globals)
        return None
    except Exception as e:
        return str(e)

def explain_error_with_llm(code):
    error_message = run_code_and_capture_error(code)
    if not error_message:
        return "✅ No error found in code."

    prompt = generate_prompt(code, error_message)

    # UPDATED NAMES FOR 2026
    models_to_try = [
        "gemini-3-flash-preview", 
        "gemini-2.5-flash", 
        "gemini-2.5-flash-lite"
    ]

    for model_name in models_to_try:
        try:
            print(f"🤖 Attempting with {model_name}...")
            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            return f"--- Results from {model_name} --- \n\n {response.text}"

        except Exception as e:
            msg = str(e).upper()
            if "429" in msg or "RESOURCE_EXHAUSTED" in msg:
                print(f"❌ {model_name} quota full. Trying next...")
                continue
            elif "404" in msg:
                print(f"❌ {model_name} name not recognized. Trying next...")
                continue
            else:
                return f"Unexpected Error: {str(e)}"

    return "🚫 All free buckets are empty for today."

if __name__ == "__main__":
    # Test with a simple bug
    buggy_code = "print(undefined_variable)"
    print(explain_error_with_llm(buggy_code))