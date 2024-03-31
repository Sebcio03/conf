import asyncio
import sys

from conf import settings
from openai import OpenAI


async def invoke(client: OpenAI, messages: list[dict]) -> None:
    stream = client.chat.completions.create(
        model=settings.model,
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
    print("\n\nAsk ChatGTP again >>> ", end="")


async def main() -> None:
    arg = " ".join(sys.argv[2:])
    client = OpenAI(api_key=settings.api_key)

    messages = [
        {"role": "system", "content": settings.system},
        {"role": "user", "content": f"{settings.user} {arg}"},
    ]
    while True:
        await invoke(client, messages)
        msg = input()
        messages.append(
            {"role": "user", "content": msg},
        )


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            """
            You have to run this script with:
                - first argument .json settings file name inside script directory
                - second argument initial call to chatgpt"

            eg. python main.py job "command to dump data postgresql"
            """
        )
        exit(1)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        ...
