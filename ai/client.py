"""
Client for communicating with llama.cpp server.
"""

import requests


class AIClient:

    def __init__(self,
                 host="127.0.0.1",
                 port=8080):

        self.url = f"http://{host}:{port}/v1/chat/completions"

    def ask(self,
            system_prompt,
            message,
            temperature=0.7):

        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            "temperature": temperature
        }

        response = requests.post(
            self.url,
            json=payload,
            timeout=300
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]
