"""
Calendar Manager voor het beheren van afspraken
"""
import json
import os
from datetime import datetime
from typing import List, Optional
from calendar import monthrange, month_name
import calendar as cal

from .event import Event


class CalendarManager:
    """Beheer kalender en afspraken"""

    def __init__(self, data_file: str = "calendar_events.json"):
        """
        Initialiseer CalendarManager

        Args:
            data_file: Bestandsnaam voor opslaan events
        """
        self.data_file = data_file
        self.events: List[Event] = []
        self.load_events()

    def add_event(self, event: Event) -> None:
        """Voeg een event toe aan de kalender"""
        self.events.append(event)
        self.save_events()

    def remove_event(self, index: int) -> bool:
        """
        Verwijder een event op basis van index

        Returns:
            True als succesvol verwijderd, False als index ongeldig
        """
        if 0 <= index < len(self.events):
            self.events.pop(index)
            self.save_events()
            return True
        return False

    def get_events_for_date(self, date: str) -> List[Event]:
        """Haal alle events op voor een specifieke datum"""
        return [event for event in self.events if event.date == date]

    def get_events_for_month(self, month: int, year: int) -> List[Event]:
        """Haal alle events op voor een specifieke maand"""
        month_events = []
        for event in self.events:
            try:
                event_date = event.get_datetime()
                if event_date.month == month and event_date.year == year:
                    month_events.append(event)
            except ValueError:
                continue
        return sorted(month_events, key=lambda e: e.get_datetime())

    def get_all_events(self) -> List[Event]:
        """Haal alle events op, gesorteerd op datum"""
        return sorted(self.events, key=lambda e: e.get_datetime())

    def save_events(self) -> None:
        """Sla events op naar JSON bestand"""
        data = [event.to_dict() for event in self.events]
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_events(self) -> None:
        """Laad events van JSON bestand"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.events = [Event.from_dict(event_data) for event_data in data]
            except (json.JSONDecodeError, KeyError):
                self.events = []
        else:
            self.events = []

    def display_month(self, month: int, year: int) -> str:
        """
        Genereer een visuele weergave van de maand

        Returns:
            String met kalender voor de maand
        """
        # Maak kalender voor de maand
        cal.setfirstweekday(cal.MONDAY)  # Start op maandag
        month_cal = cal.monthcalendar(year, month)

        # Header
        output = []
        output.append(f"\n{'='*50}")
        output.append(f"{month_name[month]} {year}".center(50))
        output.append(f"{'='*50}")
        output.append("\n  Ma  Di  Wo  Do  Vr  Za  Zo")
        output.append("-" * 50)

        # Haal events voor deze maand op
        month_events = self.get_events_for_month(month, year)
        event_dates = {event.date.split('-')[0] for event in month_events}

        # Teken kalender
        for week in month_cal:
            week_str = ""
            for day in week:
                if day == 0:
                    week_str += "    "
                else:
                    day_str = f"{day:2d}"
                    # Markeer dagen met events met een *
                    if f"{day:02d}" in event_dates:
                        day_str += "*"
                    else:
                        day_str += " "
                    week_str += day_str + " "
            output.append(week_str)

        output.append("-" * 50)
        output.append("* = Afspraak op deze dag")

        return "\n".join(output)

    def search_events(self, query: str) -> List[Event]:
        """Zoek events op basis van titel of beschrijving"""
        query_lower = query.lower()
        return [
            event for event in self.events
            if query_lower in event.title.lower() or
               query_lower in event.description.lower()
        ]
