# Simple Chat with Ollama

This project allows you to interact with a local language model using Ollama.

## Functional description

### Purpose and Overview

The program implements a command-line chat interface that allows a user to interact with a local Ollama language model (e.g., Llama 2).

Its primary functions are:
- Accepting user input in a conversational loop.
- Sending input to the Ollama API.
- Displaying model responses in real time.
- Logging all interactions and operational events to files (not to console).
- Persisting chat histories for traceability and debugging.

This is a self-contained, file-logging, terminal-based interface for local LLM interaction.

### Functional Flow Summary

1. **Script Execution**
   - The user runs the program (`python chat.py`).
   - The main function `chat_with_ollama()` is invoked.

2. **Environment Setup**
   - `setup_directories()` ensures that `data/logs/` and `data/output/` exist.
   - `configure_logging()` initializes file-based logging and disables console output.

3. **Session Start**
   - A welcome message is printed: “Welcome to the Ollama chat. Type 'exit' to quit.”
   - The chat session is logged as started.

4. **Main Chat Loop**
   - The program waits for user input (`input("You: ")`).
   - If the user types **exit**, the session closes gracefully.
   - Otherwise:
     1. The input is logged.
     2. A spinner is shown (“Working on response…”).
     3. The input is sent to the Ollama model (`ollama.chat()`).
     4. The AI response is received and logged.
     5. The response is displayed in the console as `AI: <message>`.

5. **Error Handling**
   - Any exception during model interaction is caught.
   - The error is logged with stack trace.
   - A short error message is printed to the user.

6. **Session End**
   - When the user exits, the program logs the termination event.
   - Prints “Goodbye!” and stops execution.



## Prerequisites

- Python 3.8 or higher  
- Ollama installed and configured locally

## Installation

1. **Install Ollama**:
   - Follow the instructions on the [official Ollama website](https://ollama.ai) to install it on your machine.

2. **Download the model**:
   - Once Ollama is installed, download the `llama2` model by running the following command in your terminal:
     ```bash
     ollama pull llama2
     ```

3. **Set Up Python Environment**:
   - Clone or download this repository.
   - Navigate to the project directory.
   - Install the required Python packages using `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

## VS Code Configuration

To configure VS Code and get your environment ready, follow these steps.

1. **Create the virtual environment**:

  - First, go to the project folder and run:
    ```
    python -m venv venv
    ```

2. **Activate the virtual environment**:

   It depends on your operating system (OS).

      **Linux**

      ```
      source venv/bin/activate
      ```

      **Windows (PowerShell)**

      ```
      venv\Scripts\Activate.ps1
      ```

      **Windows (Command Prompt)**

      ```
      venv\Scripts\activate
      ```

## Running the project

1. **Start Ollama**:
   - Make sure Ollama is running on your machine.
     ```bash
     ollama serve
     ```

2. **Run the script**:
   - Navigate to the directory containing `simple_chat.py` and execute it with Python:
     ```bash
     python simple_chat.py
     ```

     OR

     ```bash
     python -m app.chat.ollama_chat
     ```

3. **Interact with the model**:
   - Type your questions in the terminal. The model will reply.
   - To quit, type `exit`.

## Troubleshooting

- If you get an error saying the AI is not ready, make sure Ollama is installed and running.
- Check that the `llama2` model has been properly downloaded.
- If Ollama says ip is already in use, type on the terminal
     ```bash
     sudo systemctl stop ollama
     ollama serve
     ```

## Authors

Abel Santos