"""Explore UAP reports and richest people for unique angles."""
import csv, sys, os
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# UAP Reports
print("="*60)
print("  UAP/UFO REPORTS ANALYSIS")
print("="*60)
fp = r"D:\raw_data\kaggle\archive (50)\uap_reports.csv"
states = Counter()
shapes = Counter()
countries = Counter()
decades = Counter()
count = 0
with open(fp, encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    for row in reader:
        count += 1
        states[row.get("state","")] += 1
        shapes[row.get("shape","")] += 1
        countries[row.get("country","")] += 1
        dt = row.get("datetime","")
        if "/" in dt:
            parts = dt.split("/")
            if len(parts) >= 3:
                yr = parts[2].split()[0] if " " in parts[2] else parts[2]
                try:
                    decade = (int(yr) // 10) * 10
                    decades[decade] += 1
                except:
                    pass

print(f"Total reports: {count}")
print(f"\nTop 15 states: {states.most_common(15)}")
print(f"\nTop 10 shapes: {shapes.most_common(10)}")
print(f"\nCountries: {countries.most_common(10)}")
print(f"\nDecades: {sorted(decades.items())}")

# Richest People
print("\n" + "="*60)
print("  RICHEST PEOPLE ANALYSIS")
print("="*60)
fp2 = r"D:\raw_data\kaggle\archive (44)\richest_people_dataset.csv"
countries2 = Counter()
industries = Counter()
cities = Counter()
genders = Counter()
self_made = Counter()
with open(fp2, encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    for row in reader:
        countries2[row.get("Country","")] += 1
        industries[row.get("Industry","")] += 1
        cities[row.get("City","")] += 1
        genders[row.get("Gender","")] += 1
        self_made[row.get("Self Made","")] += 1

print(f"\nTop 15 countries: {countries2.most_common(15)}")
print(f"\nTop 10 industries: {industries.most_common(10)}")
print(f"\nTop 10 cities: {cities.most_common(10)}")
print(f"\nGender: {genders.most_common()}")
print(f"\nSelf Made: {self_made.most_common()}")

# Breakfast basket unique items and cities
print("\n" + "="*60)
print("  BREAKFAST BASKET ANALYSIS")
print("="*60)
fp3 = r"D:\raw_data\kaggle\archive (38)\breakfast basket.csv"
bb_cities = Counter()
bb_items = Counter()
bb_continents = Counter()
with open(fp3, encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    for row in reader:
        bb_cities[row.get("City","")] += 1
        bb_items[row.get("Item","")] += 1
        bb_continents[row.get("Continent","")] += 1
print(f"Cities: {bb_cities.most_common(20)}")
print(f"\nItems: {bb_items.most_common()}")
print(f"\nContinents: {bb_continents.most_common()}")

# Football: tournaments breakdown
print("\n" + "="*60)
print("  FOOTBALL RESULTS ANALYSIS")
print("="*60)
fp4 = r"D:\raw_data\kaggle\FBRESULTS26\results.csv"
tournaments = Counter()
home_teams = Counter()
fb_decades = Counter()
with open(fp4, encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    for row in reader:
        tournaments[row.get("tournament","")] += 1
        home_teams[row.get("home_team","")] += 1
        date = row.get("date","")
        if date:
            try:
                decade = (int(date[:4]) // 10) * 10
                fb_decades[decade] += 1
            except:
                pass
print(f"Top 15 tournaments: {tournaments.most_common(15)}")
print(f"\nTop 15 teams: {home_teams.most_common(15)}")
print(f"\nMatches by decade: {sorted(fb_decades.items())}")
