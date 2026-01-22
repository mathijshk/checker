#!/usr/bin/env python3
"""
Agenda Applicatie - Interactieve kalender met afspraken beheer

Een eenvoudige maar krachtige agenda tool om:
- Kalender maanden te bekijken
- Afspraken toe te voegen
- Afspraken te bekijken en te beheren
- Afspraken te zoeken
"""

import sys
from datetime import datetime
from agenda_lib.calendar_manager import CalendarManager
from agenda_lib.event import Event


def print_header():
    """Print de applicatie header"""
    print("\n" + "=" * 60)
    print(" 📅  AGENDA APPLICATIE  📅 ".center(60))
    print("=" * 60)


def print_menu():
    """Print het hoofdmenu"""
    print("\n" + "-" * 60)
    print("HOOFDMENU:")
    print("-" * 60)
    print("1. Bekijk kalender voor een maand")
    print("2. Voeg nieuwe afspraak toe")
    print("3. Bekijk alle afspraken")
    print("4. Bekijk afspraken voor een datum")
    print("5. Zoek afspraken")
    print("6. Verwijder afspraak")
    print("7. Exit")
    print("-" * 60)


def get_valid_date() -> str:
    """
    Vraag gebruiker om een geldige datum

    Returns:
        Datum in formaat DD-MM-YYYY
    """
    while True:
        date_input = input("Datum (DD-MM-YYYY): ").strip()
        try:
            datetime.strptime(date_input, "%d-%m-%Y")
            return date_input
        except ValueError:
            print("❌ Ongeldige datum! Gebruik formaat DD-MM-YYYY (bijv. 25-01-2026)")


def get_valid_time() -> str:
    """
    Vraag gebruiker om een geldige tijd

    Returns:
        Tijd in formaat HH:MM
    """
    while True:
        time_input = input("Tijd (HH:MM): ").strip()
        try:
            datetime.strptime(time_input, "%H:%M")
            return time_input
        except ValueError:
            print("❌ Ongeldige tijd! Gebruik formaat HH:MM (bijv. 14:30)")


def view_calendar(manager: CalendarManager):
    """Bekijk kalender voor een specifieke maand"""
    print("\n" + "=" * 60)
    print(" KALENDER BEKIJKEN ".center(60))
    print("=" * 60)

    current_date = datetime.now()

    print(f"\nHuidige maand: {current_date.month}/{current_date.year}")
    use_current = input("Wil je de huidige maand bekijken? (j/n): ").strip().lower()

    if use_current == 'j':
        month = current_date.month
        year = current_date.year
    else:
        while True:
            try:
                month = int(input("Maand (1-12): ").strip())
                if 1 <= month <= 12:
                    break
                print("❌ Maand moet tussen 1 en 12 zijn!")
            except ValueError:
                print("❌ Voer een geldig nummer in!")

        while True:
            try:
                year = int(input("Jaar (bijv. 2026): ").strip())
                if year > 1900:
                    break
                print("❌ Voer een geldig jaar in!")
            except ValueError:
                print("❌ Voer een geldig nummer in!")

    calendar_view = manager.display_month(month, year)
    print(calendar_view)

    # Toon events voor deze maand
    month_events = manager.get_events_for_month(month, year)
    if month_events:
        print(f"\n📋 Afspraken in deze maand: {len(month_events)}")
        print("-" * 60)
        for event in month_events:
            print(f"  • {event}")
            if event.description:
                print(f"    └─ {event.description}")


def add_event(manager: CalendarManager):
    """Voeg een nieuwe afspraak toe"""
    print("\n" + "=" * 60)
    print(" NIEUWE AFSPRAAK TOEVOEGEN ".center(60))
    print("=" * 60)

    title = input("\nTitel: ").strip()
    if not title:
        print("❌ Titel mag niet leeg zijn!")
        return

    date = get_valid_date()
    time = get_valid_time()

    description = input("Beschrijving (optioneel): ").strip()

    while True:
        try:
            duration = input("Duur in minuten (standaard 60): ").strip()
            if not duration:
                duration = 60
            else:
                duration = int(duration)
            if duration > 0:
                break
            print("❌ Duur moet positief zijn!")
        except ValueError:
            print("❌ Voer een geldig nummer in!")

    event = Event(title, date, time, description, duration)
    manager.add_event(event)

    print("\n✅ Afspraak succesvol toegevoegd!")
    print(f"   {event}")


def view_all_events(manager: CalendarManager):
    """Bekijk alle afspraken"""
    print("\n" + "=" * 60)
    print(" ALLE AFSPRAKEN ".center(60))
    print("=" * 60)

    events = manager.get_all_events()

    if not events:
        print("\n📭 Geen afspraken gevonden!")
        return

    print(f"\n📋 Totaal aantal afspraken: {len(events)}\n")

    for i, event in enumerate(events, 1):
        print(f"{i}. {event}")
        if event.description:
            print(f"   └─ {event.description}")
        print()


def view_events_for_date(manager: CalendarManager):
    """Bekijk afspraken voor een specifieke datum"""
    print("\n" + "=" * 60)
    print(" AFSPRAKEN VOOR DATUM ".center(60))
    print("=" * 60)

    date = get_valid_date()
    events = manager.get_events_for_date(date)

    if not events:
        print(f"\n📭 Geen afspraken gevonden voor {date}")
        return

    print(f"\n📋 Afspraken op {date}:\n")
    for i, event in enumerate(events, 1):
        print(f"{i}. {event.time} - {event.title} ({event.duration} min)")
        if event.description:
            print(f"   └─ {event.description}")
        print()


def search_events(manager: CalendarManager):
    """Zoek afspraken op basis van zoekterm"""
    print("\n" + "=" * 60)
    print(" AFSPRAKEN ZOEKEN ".center(60))
    print("=" * 60)

    query = input("\nZoekterm: ").strip()
    if not query:
        print("❌ Zoekterm mag niet leeg zijn!")
        return

    events = manager.search_events(query)

    if not events:
        print(f"\n📭 Geen afspraken gevonden met '{query}'")
        return

    print(f"\n🔍 Gevonden afspraken ({len(events)}):\n")
    for i, event in enumerate(events, 1):
        print(f"{i}. {event}")
        if event.description:
            print(f"   └─ {event.description}")
        print()


def delete_event(manager: CalendarManager):
    """Verwijder een afspraak"""
    print("\n" + "=" * 60)
    print(" AFSPRAAK VERWIJDEREN ".center(60))
    print("=" * 60)

    events = manager.get_all_events()

    if not events:
        print("\n📭 Geen afspraken om te verwijderen!")
        return

    print(f"\n📋 Selecteer een afspraak om te verwijderen:\n")
    for i, event in enumerate(events, 1):
        print(f"{i}. {event}")

    while True:
        try:
            choice = input("\nNummer van afspraak (0 = annuleer): ").strip()
            if not choice:
                continue
            choice = int(choice)
            if choice == 0:
                print("Verwijderen geannuleerd.")
                return
            if 1 <= choice <= len(events):
                break
            print(f"❌ Kies een nummer tussen 1 en {len(events)}!")
        except ValueError:
            print("❌ Voer een geldig nummer in!")

    event_to_delete = events[choice - 1]
    confirm = input(f"\n⚠️  Weet je zeker dat je '{event_to_delete.title}' wilt verwijderen? (j/n): ").strip().lower()

    if confirm == 'j':
        # Find the actual index in manager.events
        actual_index = manager.events.index(event_to_delete)
        manager.remove_event(actual_index)
        print("\n✅ Afspraak succesvol verwijderd!")
    else:
        print("\nVerwijderen geannuleerd.")


def main():
    """Hoofdfunctie van de agenda applicatie"""
    print_header()
    print("\nWelkom bij de Agenda Applicatie!")
    print("Beheer je afspraken en bekijk je kalender.\n")

    # Initialiseer CalendarManager
    manager = CalendarManager()

    # Hoofdloop
    while True:
        print_menu()

        choice = input("\nKies een optie (1-7): ").strip()

        if choice == '1':
            view_calendar(manager)
        elif choice == '2':
            add_event(manager)
        elif choice == '3':
            view_all_events(manager)
        elif choice == '4':
            view_events_for_date(manager)
        elif choice == '5':
            search_events(manager)
        elif choice == '6':
            delete_event(manager)
        elif choice == '7':
            print("\n" + "=" * 60)
            print(" Bedankt voor het gebruiken van de Agenda Applicatie! ".center(60))
            print("=" * 60)
            sys.exit(0)
        else:
            print("\n❌ Ongeldige keuze! Kies een nummer tussen 1 en 7.")

        input("\nDruk op Enter om door te gaan...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + "=" * 60)
        print(" Applicatie afgesloten door gebruiker ".center(60))
        print("=" * 60)
        sys.exit(0)
