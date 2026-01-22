"""
Event class voor agenda/kalender applicatie
"""
from datetime import datetime
from typing import Optional


class Event:
    """Klasse om een agenda-afspraak te representeren"""

    def __init__(self,
                 title: str,
                 date: str,
                 time: str,
                 description: str = "",
                 duration: int = 60):
        """
        Initialiseer een nieuwe afspraak

        Args:
            title: Titel van de afspraak
            date: Datum in formaat DD-MM-YYYY
            time: Tijd in formaat HH:MM
            description: Optionele beschrijving
            duration: Duur in minuten (standaard 60)
        """
        self.title = title
        self.date = date
        self.time = time
        self.description = description
        self.duration = duration

    def get_datetime(self) -> datetime:
        """Converteer date en time naar datetime object"""
        datetime_str = f"{self.date} {self.time}"
        return datetime.strptime(datetime_str, "%d-%m-%Y %H:%M")

    def to_dict(self) -> dict:
        """Converteer event naar dictionary voor opslag"""
        return {
            'title': self.title,
            'date': self.date,
            'time': self.time,
            'description': self.description,
            'duration': self.duration
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Event':
        """Maak Event object van dictionary"""
        return cls(
            title=data['title'],
            date=data['date'],
            time=data['time'],
            description=data.get('description', ''),
            duration=data.get('duration', 60)
        )

    def __str__(self) -> str:
        """String representatie van event"""
        return f"{self.date} {self.time} - {self.title} ({self.duration} min)"

    def __repr__(self) -> str:
        return f"Event('{self.title}', '{self.date}', '{self.time}')"
