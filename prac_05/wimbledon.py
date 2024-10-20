"""
Wimbledon
Estimate: 20 minutes
Actual:   40 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read data and print champions and countries"""
    champion_data = load_champion_data(FILENAME)
    champion_wins, countries = count_champion_data(champion_data)
    display_champion_data(champion_wins, countries)


def count_champion_data(champion_data):
    """Create champion dictionary and set of countries from champion_data"""
    champion_wins = {}
    champion_countries = set()
    for row in champion_data:
        champion_countries.add(row[1])
        try:
            champion_wins[row[2]] += 1
        except KeyError:
            champion_wins[row[2]] = 1
    return champion_wins, champion_countries


def display_champion_data(champion_wins, champion_countries):
    """Display winners and countries"""
    print("Wimbledon Champions:")
    for champion, wins in champion_wins.items():
        print(f"{champion} {wins}")
    country_count = len(champion_countries)
    print(f"\nThese {country_count} countries have won Wimbledon:")
    print(" ".join(country for country in sorted(champion_countries)))


def load_champion_data(filename):
    """Load championship data from a CSV file and return it as a list"""
    champion_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            row = line.strip().split(',')
            champion_data.append(row)
    return champion_data


main()
