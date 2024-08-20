from pydantic import BaseModel
import os
import openai
from openai import OpenAI
from pydantic import Field
from enum import Enum
from typing import List, Union, Dict


"""
duration: An integer representing the total duration of the meditation in milliseconds.
focus_area: A string describing the focus or theme of the meditation (e.g., "relaxation", "focus").
phrases: A list of dictionaries, where each dictionary represents a phrase in the meditation. Each phrase has:
text: The actual text of the meditation instruction.
pause: The duration of the pause (in milliseconds) after the instruction is spoken.
Field(...): Tells Pydantic that these fields are required (... is a shortcut for that).
schema_extra: Provides an example JSON structure for documentation purposes, making it clear what the expected output should look like.

"""

class MeditationType(str, Enum):
    duration: int = Field(..., description="Total duration in milliseconds")  
    focus_area: str = Field(..., description="Focus area of the meditation")  
    phrases: List[Dict[str, str]] = Field(..., description="List of dictionaries with text and pause in milliseconds") 

    class Config:
        json_schema_extra = {
            "example": {
                "duration": 45000,
                "focus_area": "relaxation",
                "phrases": [
                    {"text": "Welcome to this meditation, find a comfortable position and close your eyes.", "pause": "2000"},
                    {"text": "Bring your attention to your breath, noticing the rise and fall of your chest.", "pause": "3000"},
                ]
            }
        }


class Instruction(BaseModel):
    text: str
    duration: int


class Pause(BaseModel):
    duration: int


class Meditation(BaseModel):
    type: MeditationType
    duration: int = Field(..., description="Total duration in seconds")
    instructions: List[Instruction] = Field(..., description="List of instructions")


def yi_generate(user_query):
    client = openai.OpenAI(api_key="OPENAI_KEY")


    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
        {
            "role": "system",
            "content": """You are a helpful assistant. You can create guided meditations with specific instructions and timings in the desired output format.
            Use the `Meditation` function to create a meditation.
            Here's an example of the expected output:
            ```json
            {
                "duration": 45000,
                "focus_area": "relaxation",
                "phrases": [
                    {"text": "Welcome to this meditation...", "pause": "2000"},
                    {"text": "Bring your attention to your breath...", "pause": "3000"}
                ]
            }
            ```
            """,
        },
        {
            "role": "user",
            "content": user_query,
        },
    ],
        tools=[
            openai.pydantic_function_tool(Meditation),
        ],
    )


    if completion.choices[0].message.tool_calls:
        meditation = completion.choices[0].message.tool_calls[0].function.parsed_arguments
        return meditation
    
    else:
        print("No tool calls found.")