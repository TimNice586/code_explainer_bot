# 🧠 Code Explainer Bot — Error-Focused Python Assistant

## 📊 Project Overview

This project is a proof of concept for a **Code Explainer Bot** designed to help learners understand **Python errors** without receiving direct solutions.

The bot analyzes faulty Python code, captures the resulting error, and generates a **conceptual explanation** using a Large Language Model (LLM).  
It is intentionally designed to act as a **teaching assistant**, similar to how a BeCode coach would explain an error without writing the correct code for the student.

The bot supports **two usage modes**:
- Analyzing a **random faulty Python script** from a predefined dataset
- Analyzing **user-provided Python code**

---

## 🎯 Key Objectives

- **Pedagogical Support**  
  Help learners understand Python errors instead of solving them automatically.

- **Error Analysis**  
  Clearly explain what an error means and why it occurred.

- **Conceptual Guidance**  
  Suggest how to fix the issue conceptually without providing working code.

- **Prompt Control**  
  Enforce strict LLM constraints to prevent solution leakage.

- **Automation & Reproducibility**  
  Process multiple error cases in a consistent, testable pipeline.

---

## 🤖 Bot Behavior & Constraints

The bot **must** adhere to the following rules:

- ❌ Must NOT generate corrected or working code  
- ✅ Must explain **what the error means**  
- ✅ Must explain **why it happened**  
- ✅ Must suggest **conceptual fixes only**  
- ✅ Must behave as a **teaching assistant**, not a code generator  

These constraints are enforced through **prompt engineering**, not post-processing.

---

## 🔍 Technical Highlights

### 🔧 Error Processing Pipeline

1. Python code is loaded (random script or user input)  
2. The code is executed in a controlled environment  
3. Python exceptions are captured (syntax, runtime, logic errors)  
4. The code and error message are sent to the LLM  
5. The LLM generates a structured explanation  
6. Results are saved to a Markdown file for review  

---

### 🧠 Prompt Design

The LLM is instructed to explain:

- What the error means  
- Why it occurred  
- How the student can fix it conceptually  

While explicitly avoiding:

- Providing corrected code  
- Writing example implementations  
- Giving copy-paste solutions  

This ensures the bot supports learning rather than shortcutting it.

---

## 🔄 Usage Modes

### 🎲 Mode 1: Random Faulty Script

- A Python file is randomly selected from `data/faulty_scripts/`
- The script is executed and analyzed automatically
- Useful for:
  - Coach demonstrations
  - Testing common beginner mistakes
  - Automated evaluation

### ✍️ Mode 2: User-Provided Code

- The user provides a Python code snippet directly
- The snippet is analyzed in the same pipeline
- Useful for:
  - Student debugging
  - One-off explanations
  - Interactive learning

Both modes share the **same error handling and explanation logic**.

---

## 🧪 Error Types Covered

The project includes at least **five common Python error types**:

- SyntaxError  
- NameError  
- TypeError  
- ZeroDivisionError  
- IndexError  

Additional error cases can be added easily.

---

## 📦 File Structure

```
code_explainer_bot/
│
├── data/
│ └── faulty_scripts/
│ ├── error1.py
│ ├── error2.py
│ ├── error3.py
│ ├── error4.py
│ └── error5.py
│
├── outputs/
│ └── explanations.md
│
├── src/
│ ├── file_reader.py # Loads Python files from disk
│ ├── prompt_template.py # LLM prompt construction
│ ├── error_explainer.py # Error execution & LLM interaction
│ └── main.py # Project orchestration & mode selection
│
├── requirements.txt
└── README.md
```

## 🚀 How to Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```
2️⃣ Run the bot

```bash
python src/main.py
```

At runtime, the user can:

- Analyze a **random faulty script**
- Provide **custom Python code**

---

## 📄 View Results

Generated explanations are written to:

```text
outputs/explanations.md
```

Each entry contains:

- **The original code snippet**  
- **The captured Python error**  
- **A structured conceptual explanation**

---

###  Timeline
- **Duration:** 2 hours  
- **Focus:** Educational tooling, prompt engineering, error analysis  
- **Outcome:** A reusable proof of concept for a BeCode-style Python teaching assistant

---

### 👤 Author
**Tim De Nijs**  
Data Science & AI — BeCode Ghent (2025–2026)
