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


# Albert Heijn kleuren (ANSI codes met RGB voor true color support)
class AHColors:
    """Albert Heijn huisstijl kleuren"""
    # Albert Heijn blauw: RGB(0, 113, 206) - #0071CE
    AH_BLUE = '\033[38;2;0;113;206m'
    # Lichtblauw accent
    AH_LIGHT_BLUE = '\033[38;2;100;180;255m'
    # Wit voor text
    WHITE = '\033[97m'
    # Bold voor nadruk
    BOLD = '\033[1m'
    # Reset
    RESET = '\033[0m'
    # Groen voor succes (behouden voor ✅)
    GREEN = '\033[92m'
    # Rood voor errors (behouden voor ❌)
    RED = '\033[91m'
    # Geel voor waarschuwingen
    YELLOW = '\033[93m'

    @staticmethod
    def header(text: str) -> str:
        """Maak een header in AH-stijl"""
        return f"{AHColors.AH_BLUE}{AHColors.BOLD}{text}{AHColors.RESET}"

    @staticmethod
    def accent(text: str) -> str:
        """Maak accent tekst in lichtblauw"""
        return f"{AHColors.AH_LIGHT_BLUE}{text}{AHColors.RESET}"

    @staticmethod
    def success(text: str) -> str:
        """Maak succes tekst in groen"""
        return f"{AHColors.GREEN}{text}{AHColors.RESET}"

    @staticmethod
    def error(text: str) -> str:
        """Maak error tekst in rood"""
        return f"{AHColors.RED}{text}{AHColors.RESET}"


def print_header():
    """Print de applicatie header"""
    print("\n" + AHColors.header("=" * 60))
    print(AHColors.header(" 📅  ALBERT HEIJN AGENDA  📅 ".center(60)))
    print(AHColors.header("=" * 60))


def print_menu():
    """Print het hoofdmenu"""
    print("\n" + AHColors.accent("-" * 60))
    print(AHColors.header("HOOFDMENU:"))
    print(AHColors.accent("-" * 60))
    print(AHColors.accent("1.") + " Bekijk kalender voor een maand")
    print(AHColors.accent("2.") + " Voeg nieuwe afspraak toe")
    print(AHColors.accent("3.") + " Bekijk alle afspraken")
    print(AHColors.accent("4.") + " Bekijk afspraken voor een datum")
    print(AHColors.accent("5.") + " Zoek afspraken")
    print(AHColors.accent("6.") + " Verwijder afspraak")
    print(AHColors.accent("7.") + " Exit")
    print(AHColors.accent("-" * 60))


def get_valid_date() -> str:
    """
    Vraag gebruiker om een geldige datum

    Returns:
        Datum in formaat DD-MM-YYYY
    """
    while True:
        date_input = input(AHColors.accent("Datum (DD-MM-YYYY): ")).strip()
        try:
            datetime.strptime(date_input, "%d-%m-%Y")
            return date_input
        except ValueError:
            print(AHColors.error("❌ Ongeldige datum! Gebruik formaat DD-MM-YYYY (bijv. 25-01-2026)"))


def get_valid_time() -> str:
    """
    Vraag gebruiker om een geldige tijd

    Returns:
        Tijd in formaat HH:MM
    """
    while True:
        time_input = input(AHColors.accent("Tijd (HH:MM): ")).strip()
        try:
            datetime.strptime(time_input, "%H:%M")
            return time_input
        except ValueError:
            print(AHColors.error("❌ Ongeldige tijd! Gebruik formaat HH:MM (bijv. 14:30)"))


def view_calendar(manager: CalendarManager):
    """Bekijk kalender voor een specifieke maand"""
    print("\n" + AHColors.header("=" * 60))
    print(AHColors.header(" KALENDER BEKIJKEN ".center(60)))
    print(AHColors.header("=" * 60))

    current_date = datetime.now()

    print(f"\n{AHColors.accent('Huidige maand:')} {current_date.month}/{current_date.year}")
    use_current = input(AHColors.accent("Wil je de huidige maand bekijken? (j/n): ")).strip().lower()

    if use_current == 'j':
        month = current_date.month
        year = current_date.year
    else:
        while True:
            try:
                month = int(input(AHColors.accent("Maand (1-12): ")).strip())
                if 1 <= month <= 12:
                    break
                print(AHColors.error("❌ Maand moet tussen 1 en 12 zijn!"))
            except ValueError:
                print(AHColors.error("❌ Voer een geldig nummer in!"))

        while True:
            try:
                year = int(input(AHColors.accent("Jaar (bijv. 2026): ")).strip())
                if year > 1900:
                    break
                print(AHColors.error("❌ Voer een geldig jaar in!"))
            except ValueError:
                print(AHColors.error("❌ Voer een geldig nummer in!"))

    calendar_view = manager.display_month(month, year)
    print(calendar_view)

    # Toon events voor deze maand
    month_events = manager.get_events_for_month(month, year)
    if month_events:
        print(f"\n{AHColors.AH_BLUE}📋 Afspraken in deze maand: {len(month_events)}{AHColors.RESET}")
        print(AHColors.accent("-" * 60))
        for event in month_events:
            print(f"  {AHColors.AH_LIGHT_BLUE}•{AHColors.RESET} {event}")
            if event.description:
                print(f"    {AHColors.accent('└─')} {event.description}")


def add_event(manager: CalendarManager):
    """Voeg een nieuwe afspraak toe"""
    print("\n" + AHColors.header("=" * 60))
    print(AHColors.header(" NIEUWE AFSPRAAK TOEVOEGEN ".center(60)))
    print(AHColors.header("=" * 60))

    title = input(f"\n{AHColors.accent('Titel: ')}").strip()
    if not title:
        print(AHColors.error("❌ Titel mag niet leeg zijn!"))
        return

    date = get_valid_date()
    time = get_valid_time()

    description = input(AHColors.accent("Beschrijving (optioneel): ")).strip()

    while True:
        try:
            duration = input(AHColors.accent("Duur in minuten (standaard 60): ")).strip()
            if not duration:
                duration = 60
            else:
                duration = int(duration)
            if duration > 0:
                break
            print(AHColors.error("❌ Duur moet positief zijn!"))
        except ValueError:
            print(AHColors.error("❌ Voer een geldig nummer in!"))

    event = Event(title, date, time, description, duration)
    manager.add_event(event)

    print(AHColors.success("\n✅ Afspraak succesvol toegevoegd!"))
    print(f"   {AHColors.AH_BLUE}{event}{AHColors.RESET}")


def view_all_events(manager: CalendarManager):
    """Bekijk alle afspraken"""
    print("\n" + AHColors.header("=" * 60))
    print(AHColors.header(" ALLE AFSPRAKEN ".center(60)))
    print(AHColors.header("=" * 60))

    events = manager.get_all_events()

    if not events:
        print(f"\n{AHColors.YELLOW}📭 Geen afspraken gevonden!{AHColors.RESET}")
        return

    print(f"\n{AHColors.AH_BLUE}📋 Totaal aantal afspraken: {len(events)}{AHColors.RESET}\n")

    for i, event in enumerate(events, 1):
        print(f"{AHColors.accent(str(i)+'.')} {event}")
        if event.description:
            print(f"   {AHColors.accent('└─')} {event.description}")
        print()


def view_events_for_date(manager: CalendarManager):
    """Bekijk afspraken voor een specifieke datum"""
    print("\n" + AHColors.header("=" * 60))
    print(AHColors.header(" AFSPRAKEN VOOR DATUM ".center(60)))
    print(AHColors.header("=" * 60))

    date = get_valid_date()
    events = manager.get_events_for_date(date)

    if not events:
        print(f"\n{AHColors.YELLOW}📭 Geen afspraken gevonden voor {date}{AHColors.RESET}")
        return

    print(f"\n{AHColors.AH_BLUE}📋 Afspraken op {date}:{AHColors.RESET}\n")
    for i, event in enumerate(events, 1):
        print(f"{AHColors.accent(str(i)+'.')} {event.time} - {event.title} ({event.duration} min)")
        if event.description:
            print(f"   {AHColors.accent('└─')} {event.description}")
        print()


def search_events(manager: CalendarManager):
    """Zoek afspraken op basis van zoekterm"""
    print("\n" + AHColors.header("=" * 60))
    print(AHColors.header(" AFSPRAKEN ZOEKEN ".center(60)))
    print(AHColors.header("=" * 60))

    query = input(f"\n{AHColors.accent('Zoekterm: ')}").strip()
    if not query:
        print(AHColors.error("❌ Zoekterm mag niet leeg zijn!"))
        return

    events = manager.search_events(query)

    if not events:
        print(f"\n{AHColors.YELLOW}📭 Geen afspraken gevonden met '{query}'{AHColors.RESET}")
        return

    print(f"\n{AHColors.AH_BLUE}🔍 Gevonden afspraken ({len(events)}):{AHColors.RESET}\n")
    for i, event in enumerate(events, 1):
        print(f"{AHColors.accent(str(i)+'.')} {event}")
        if event.description:
            print(f"   {AHColors.accent('└─')} {event.description}")
        print()


def delete_event(manager: CalendarManager):
    """Verwijder een afspraak"""
    print("\n" + AHColors.header("=" * 60))
    print(AHColors.header(" AFSPRAAK VERWIJDEREN ".center(60)))
    print(AHColors.header("=" * 60))

    events = manager.get_all_events()

    if not events:
        print(f"\n{AHColors.YELLOW}📭 Geen afspraken om te verwijderen!{AHColors.RESET}")
        return

    print(f"\n{AHColors.AH_BLUE}📋 Selecteer een afspraak om te verwijderen:{AHColors.RESET}\n")
    for i, event in enumerate(events, 1):
        print(f"{AHColors.accent(str(i)+'.')} {event}")

    while True:
        try:
            choice = input(f"\n{AHColors.accent('Nummer van afspraak (0 = annuleer): ')}").strip()
            if not choice:
                continue
            choice = int(choice)
            if choice == 0:
                print(AHColors.YELLOW + "Verwijderen geannuleerd." + AHColors.RESET)
                return
            if 1 <= choice <= len(events):
                break
            print(AHColors.error(f"❌ Kies een nummer tussen 1 en {len(events)}!"))
        except ValueError:
            print(AHColors.error("❌ Voer een geldig nummer in!"))

    event_to_delete = events[choice - 1]
    confirm = input(f"\n{AHColors.YELLOW}⚠️  Weet je zeker dat je '{event_to_delete.title}' wilt verwijderen? (j/n): {AHColors.RESET}").strip().lower()

    if confirm == 'j':
        # Find the actual index in manager.events
        actual_index = manager.events.index(event_to_delete)
        manager.remove_event(actual_index)
        print(AHColors.success("\n✅ Afspraak succesvol verwijderd!"))
    else:
        print(f"\n{AHColors.YELLOW}Verwijderen geannuleerd.{AHColors.RESET}")


def main():
    """Hoofdfunctie van de agenda applicatie"""
    print_header()
    print(f"\n{AHColors.AH_BLUE}Welkom bij de Albert Heijn Agenda Applicatie!{AHColors.RESET}")
    print(f"{AHColors.accent('Beheer je afspraken en bekijk je kalender.')}\n")

    # Initialiseer CalendarManager
    manager = CalendarManager()

    # Hoofdloop
    while True:
        print_menu()

        choice = input(f"\n{AHColors.accent('Kies een optie (1-7): ')}").strip()

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
            print("\n" + AHColors.header("=" * 60))
            print(AHColors.header(" Bedankt voor het gebruiken van de AH Agenda! ".center(60)))
            print(AHColors.header("=" * 60))
            sys.exit(0)
        else:
            print(AHColors.error("\n❌ Ongeldige keuze! Kies een nummer tussen 1 en 7."))

        input(f"\n{AHColors.accent('Druk op Enter om door te gaan...')}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + AHColors.header("=" * 60))
        print(AHColors.header(" Applicatie afgesloten door gebruiker ".center(60)))
        print(AHColors.header("=" * 60))
        sys.exit(0)
