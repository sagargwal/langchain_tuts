'''
if the input is not a stuctured text but something like a code or markdown file 
to split that also we use recursive text splitters 
we have to give language as an input here
'''

from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = '''
import random

class Event:
    def __init__(self, name, venue, time):
        self.name = name
        self.venue = venue
        self.time = time

    def display_details(self):
        print("📌 Event Details")
        print(f"Name  : {self.name}")
        print(f"Venue: {self.venue}")
        print(f"Time : {self.time}")

class EventPlanner:
    def __init__(self):
        self.events = ["Alumni Meet", "Campus Tour", "Cultural Night", "Dinner"]
        self.venues = ["OAT", "Dogra Hall", "Hostel Lawns", "Sports Complex"]
        self.times = ["4:00 PM", "5:30 PM", "7:00 PM"]

    def create_random_event(self):
        return Event(
            name=random.choice(self.events),
            venue=random.choice(self.venues),
            time=random.choice(self.times)
        )

if __name__ == "__main__":
    planner = EventPlanner()
    event = planner.create_random_event()
    event.display_details()

'''

spliter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 200,
    chunk_overlap = 0
)

chunk = spliter.split_text(text)
print(chunk)