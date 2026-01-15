from pathlib import Path
import random

from file_reader import read_python_files
from error_explainer import explain_error_with_llm

def read_user_code():
    """
    Reads multi-line user input until the user types 'the end'.
    """
    print("Please enter your code below.")
    print('Type "the end" on a new line to finish.\n')

    lines = []
    while True:
        line = input()
        if line.strip().lower() == "the end":
            break
        lines.append(line)

    return "\n".join(lines)


# -----------------------------
# User choice
# -----------------------------
print("What would you like to do?")
print("1) Load a random faulty script")
print("2) Provide your own code")

choice = input("Enter 1 or 2: ").strip()

# -----------------------------
# Option 1: Random faulty script
# -----------------------------
if choice == "1":
    faulty_folder = Path(__file__).parent.parent / "data/faulty_scripts"
    code_files = read_python_files(faulty_folder)

    filename, code = random.choice(list(code_files.items()))
    title = f"Random faulty script: {filename}"

# -----------------------------
# Option 2: User-provided code
# -----------------------------
elif choice == "2":
    code = read_user_code()
    title = "User-provided code"

else:
    print("Invalid choice. Exiting.")
    exit(1)

# -----------------------------
# Explain the error
# -----------------------------
explanation = explain_error_with_llm(code)

# -----------------------------
# Write result to markdown
# -----------------------------
output_file = Path(__file__).parent.parent / "outputs/explanations.md"

with open(output_file, "w") as f:
    f.write(f"# {title}\n\n")
    f.write("```python\n")
    f.write(code)
    f.write("\n```\n\n")
    f.write("## Explanation\n\n")
    f.write(explanation)

print("\nExplanation written to outputs/explanations.md")
