""" Ollama AI demo """

import sys
import ollama


MODEL: str = "mistral:7b-instruct"


stream = ollama.chat(
    model=MODEL,
    messages=[{"role": "user", "content": sys.argv[1]}],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)

print("\n")
