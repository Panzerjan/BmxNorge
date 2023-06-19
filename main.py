from bmx.comi import CommissionerManager
from bmx.race import RaceManager


def main():
    path = "./files/comi.json"
    filepath = "./files/race.json"
    manager = RaceManager(filepath)

    races_to_add = [{'location': 'Raade Bmx',
                     'type': 'National', 'date': '02072023'}]

    manager.add_race(races_to_add)
    manager.add_country_to_races()
    manager.add_description_to_races()


if __name__ == "__main__":
    main()
