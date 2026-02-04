from pydantic import BaseModel
from typing import List


# class GetPlacesRequest(BaseModel):
#     destinationCity: str
#     budget: int
#     tripDuration: int
#     peopleCount: int
#     cuisineType: str
#     travelStyle: str
#     activities: List[str]
class GetPlacesRequest(BaseModel):
    destinationCity: str
    budget: int
    tripDuration: int
    peopleCount: int
    cuisineType: str
    travelStyle: str
    activities: List[str]

    accommodationType: str = "mid-range hotels"
    transportationType: str = "public transport"
    language: str = "English"
