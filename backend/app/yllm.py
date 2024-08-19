from pydantic import BaseModel
import os
import openai
from openai import OpenAI
from pydantic import Field
from enum import Enum
from typing import List, Union, Dict

class MeditationType(str, Enum):
    mindfulness = "mindfulness"
    breathing = "breathing"
    body_scan = "body_scan"


class Instruction(BaseModel):
    text: str
    duration: int  # Duration in seconds


class Pause(BaseModel):
    duration: int  # Duration in seconds


class Meditation(BaseModel):
    type: MeditationType
    duration: int  # Total duration in seconds
    instructions: List[Union[Instruction, Pause]]


def main():
    client = openai.OpenAI(api_key="OPENAI_KEY")

    completion = client.beta.chat.completions.parse(
        model="gpt-4-1106-preview",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. You can create guided meditations with specific instructions and timings.",
            },
            {
                "role": "user",
                "content": "Can you make a 45-second mindfulness meditation?",
            },
        ],
        tools=[
            openai.pydantic_function_tool(Meditation),
        ],
    )


    meditation = completion.choices[0].message.tool_calls[0].function.parsed_arguments

    print(meditation)
    for i, instruction_or_pause in enumerate(meditation.instructions):
        print(f"Step {i+1}:")

        if isinstance(instruction_or_pause, Instruction):
            print(f"  Text: {instruction_or_pause.text}")
            print(f"  Duration: {instruction_or_pause.duration} seconds")
        elif isinstance(instruction_or_pause, Pause):
            print(f"  Pause: {instruction_or_pause.duration} seconds")

        print("-" * 20)


if __name__ == "__main__":
    main()


