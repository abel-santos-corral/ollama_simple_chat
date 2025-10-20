"""
Ollama Chat Interface
---------------------
A simple CLI chat interface for interacting with the Ollama API.
Logs all interactions to data/logs/ and saves chat history to data/output/.
"""
import os
from typing import Dict, Any
import ollama
from loguru import logger
logger.remove()  # Remove default console handler immediately
from datetime import datetime
from alive_progress import alive_bar

# Constants
MODEL_NAME: str = "llama2"
LOG_DIR: str = "data/logs"
OUTPUT_DIR: str = "data/output"
LOG_FORMAT: str = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
MAX_LOG_FILES: int = 10  # Configurable rotation limit

def setup_directories() -> None:
    """Ensure data/logs/ and data/output/ directories exist."""
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    logger.debug(f"Directories {LOG_DIR} and {OUTPUT_DIR} ensured.")

def configure_logging() -> None:
    """
    Configure loguru to save logs to data/logs/chat_{date}.log.
    Logs are rotated daily, with a maximum of MAX_LOG_FILES files.
    Console logging is disabled.
    """
    log_filename: str = f"{LOG_DIR}/chat_{datetime.now().strftime('%Y-%m-%d')}.log"
    logger.remove()  # Remove the default console handler
    logger.add(
        log_filename,
        rotation="1 day",
        retention=f"{MAX_LOG_FILES} days",
        level="INFO",
        format=LOG_FORMAT,
        enqueue=True,
    )
    logger.info("Logging configured.")

def chat_with_ollama() -> None:
    """
    Main chat function. Logs all interactions and saves chat history.
    """
    configure_logging()  # move this first
    setup_directories()
    configure_logging()
    logger.info("=== Starting Ollama Chat Session ===")
    print("Welcome to the Ollama chat. Type 'exit' to quit.")

    while True:
        user_input: str = input("You: ").strip()
        if user_input.lower() == "exit":
            logger.info("User requested to exit the chat.")
            print("Goodbye!")
            break

        try:
            logger.info(f"User input: {user_input}")
            with alive_bar(spinner="classic", title="Working on response...") as bar:
                response: Dict[str, Any] = ollama.chat(
                    model=MODEL_NAME,
                    messages=[{"role": "user", "content": user_input}],
                )
                bar()  # Update spinner
            ai_response: str = response["message"]["content"]
            logger.info(f"AI response: {ai_response}")
            print(f"AI: {ai_response}")
        except Exception as error:
            logger.error(f"API call failed: {error}", exc_info=True)
            print(f"Error: {error}")

if __name__ == "__main__":
    chat_with_ollama()
