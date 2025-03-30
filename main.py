import anthropic
from dotenv import load_dotenv
import requests
import os

if __name__ == '__main__':

    load_dotenv()

    CLAUDE_API_KEY = os.getenv("ANTHROPIC_API_KEY")

    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=300,
        temperature=1,
        system="You are a world-class poet. Respond only with short poems.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "How do I begin learning about DDQN's?"
                    }
                ]
            }
        ]
    )
    print(message.content)