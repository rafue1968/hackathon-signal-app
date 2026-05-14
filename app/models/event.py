from pydantic import BaseModel

class Event(BaseModel):
    title: str
    city: str
    category: str


    def match_event(self, preferences):
        return self.category in preferences