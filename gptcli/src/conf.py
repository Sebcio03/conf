import json
import os
import sys

from pydantic import BaseModel

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


class Settings(BaseModel):
    api_key: str = os.environ.get("OPENAI_API_KEY")
    model: str = "gpt-4"
    system: str = "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."
    user: str = ""


def load_settings():
    with open(f"{DIR_PATH}/{sys.argv[1]}.json", "r") as f:
        return Settings(**json.load(f))


settings = load_settings()
