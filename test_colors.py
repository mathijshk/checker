#!/usr/bin/env python3
"""
Test script om Albert Heijn kleuren te demonstreren
"""

# Albert Heijn kleuren (ANSI codes)
class AHColors:
    """Albert Heijn huisstijl kleuren"""
    AH_BLUE = '\033[38;2;0;113;206m'
    AH_LIGHT_BLUE = '\033[38;2;100;180;255m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'

print("\n" + "=" * 60)
print("Albert Heijn Kleuren Demo")
print("=" * 60 + "\n")

print(f"{AHColors.AH_BLUE}{AHColors.BOLD}Dit is Albert Heijn blauw (hoofdkleur){AHColors.RESET}")
print(f"{AHColors.AH_LIGHT_BLUE}Dit is lichtblauw (accent kleur){AHColors.RESET}")
print(f"{AHColors.GREEN}✅ Dit is groen (succes){AHColors.RESET}")
print(f"{AHColors.RED}❌ Dit is rood (errors){AHColors.RESET}")
print(f"{AHColors.YELLOW}⚠️  Dit is geel (waarschuwingen){AHColors.RESET}")

print("\n" + AHColors.AH_BLUE + "=" * 60 + AHColors.RESET)
print(AHColors.AH_BLUE + AHColors.BOLD + " HEADER VOORBEELD ".center(60) + AHColors.RESET)
print(AHColors.AH_BLUE + "=" * 60 + AHColors.RESET)

print("\n" + AHColors.AH_LIGHT_BLUE + "-" * 60 + AHColors.RESET)
print(AHColors.AH_BLUE + "MENU:" + AHColors.RESET)
print(AHColors.AH_LIGHT_BLUE + "1." + AHColors.RESET + " Optie 1")
print(AHColors.AH_LIGHT_BLUE + "2." + AHColors.RESET + " Optie 2")
print(AHColors.AH_LIGHT_BLUE + "-" * 60 + AHColors.RESET)

print("\n✅ Kleuren test voltooid!\n")
