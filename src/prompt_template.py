def generate_prompt(code_snippet, error_message):
    """
    Returns a formatted prompt for the LLM.
    The LLM should explain the error without giving full solutions.
    """
    prompt = f"""
You are a teaching assistant. A student wrote the following Python code:

IMPORTANT RULES:
- Do NOT write any Python code
- Do NOT suggest exact syntax
- Do NOT show corrected versions of the code
- Explain using plain language only

{code_snippet}

It produced the following error:

{error_message}

Explain:
1. What the error means
2. Why it happened
3. How the student can conceptually fix it (do NOT provide full working code)
"""
    return prompt
