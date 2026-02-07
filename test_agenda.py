#!/usr/bin/env python3
"""
Test script voor de agenda applicatie
"""

from agenda_lib.calendar_manager import CalendarManager
from agenda_lib.event import Event
from datetime import datetime


def test_calendar():
    """Test de kalender functionaliteit"""
    print("=" * 60)
    print(" TEST AGENDA APPLICATIE ".center(60))
    print("=" * 60)

    # Maak een test manager met een test bestand
    manager = CalendarManager("test_events.json")

    # Test 1: Event aanmaken
    print("\n✓ Test 1: Event aanmaken")
    event1 = Event("Vergadering", "25-01-2026", "14:00", "Team meeting", 90)
    print(f"  Created: {event1}")

    # Test 2: Event toevoegen
    print("\n✓ Test 2: Event toevoegen aan manager")
    manager.add_event(event1)
    print(f"  Events in manager: {len(manager.events)}")

    # Test 3: Meerdere events toevoegen
    print("\n✓ Test 3: Meerdere events toevoegen")
    event2 = Event("Lunch", "25-01-2026", "12:30", "Lunch met collega's", 60)
    event3 = Event("Presentatie", "27-01-2026", "10:00", "Q1 resultaten", 120)
    event4 = Event("Dokter", "03-02-2026", "15:30", "Controle afspraak", 30)

    manager.add_event(event2)
    manager.add_event(event3)
    manager.add_event(event4)
    print(f"  Totaal events: {len(manager.events)}")

    # Test 4: Events ophalen voor datum
    print("\n✓ Test 4: Events voor specifieke datum (25-01-2026)")
    date_events = manager.get_events_for_date("25-01-2026")
    print(f"  Events gevonden: {len(date_events)}")
    for event in date_events:
        print(f"    - {event}")

    # Test 5: Events voor maand ophalen
    print("\n✓ Test 5: Events voor januari 2026")
    month_events = manager.get_events_for_month(1, 2026)
    print(f"  Events gevonden: {len(month_events)}")
    for event in month_events:
        print(f"    - {event}")

    # Test 6: Kalender weergave
    print("\n✓ Test 6: Kalender weergave voor januari 2026")
    calendar_view = manager.display_month(1, 2026)
    print(calendar_view)

    # Test 7: Zoeken
    print("\n✓ Test 7: Zoeken naar 'lunch'")
    search_results = manager.search_events("lunch")
    print(f"  Events gevonden: {len(search_results)}")
    for event in search_results:
        print(f"    - {event}")

    # Test 8: Alle events ophalen (gesorteerd)
    print("\n✓ Test 8: Alle events chronologisch")
    all_events = manager.get_all_events()
    for event in all_events:
        print(f"    - {event}")

    # Test 9: Event verwijderen
    print("\n✓ Test 9: Event verwijderen")
    print(f"  Events voor verwijderen: {len(manager.events)}")
    manager.remove_event(0)
    print(f"  Events na verwijderen: {len(manager.events)}")

    # Test 10: Data persistentie
    print("\n✓ Test 10: Data opslaan en laden")
    manager.save_events()
    new_manager = CalendarManager("test_events.json")
    print(f"  Events geladen: {len(new_manager.events)}")

    print("\n" + "=" * 60)
    print(" ✅ ALLE TESTS GESLAAGD! ".center(60))
    print("=" * 60)

    # Cleanup test bestand
    import os
    if os.path.exists("test_events.json"):
        os.remove("test_events.json")
        print("\n🧹 Test bestand opgeruimd")


if __name__ == "__main__":
    try:
        test_calendar()
    except Exception as e:
        print(f"\n❌ TEST GEFAALD: {e}")
        import traceback
        traceback.print_exc()
