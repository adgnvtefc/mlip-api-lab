import json
import os
from typing import Any, Dict
from litellm import completion
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# You can replace these with other models as needed but this is the one we suggest for this lab.
MODEL = "gpt-4o-mini"


def get_itinerary(destination: str) -> Dict[str, Any]:
    """
    Returns a JSON-like dict with keys:
      - destination
      - price_range
      - ideal_visit_times
      - top_attractions
    """
    # implement litellm call here to generate a structured travel itinerary for the given destination

    # See https://docs.litellm.ai/docs/ for reference.

    class DestinationTingy(BaseModel):
        destination: str
        price_range: str
        ideal_visit_times: list[str]
        top_attractions: list[str]
    
    messages= [{"role": "system", "content": "You are a travel assistant that provides detailed travel itineraries."},
               {"role": "user", "content": f"Create a travel itinerary for {destination} including price range, ideal visit times, and top attractions."}]

    response = completion(
        model=MODEL,
        response_format=DestinationTingy,
        messages=messages
    )

    data = response.choices[0].message.content
    
    return data
