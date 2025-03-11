import json
import sys
from armor import Armor
from result import Result
from search_criteria import SearchCriteria
import itertools
import time

search_criteria = SearchCriteria(
[
    { 'Arkveld\'s Hunger': 2 },
    { 'Weakness Exploit': 5 },
    { 'Quick Sheathe': 2 },
    { 'Agitator': 3 }
], [7, 1, 0])

def main():
    start = time.time()

    print(search_criteria)

    # load data
    heads = read_armor_data('HELM')
    chests = read_armor_data('BODY')
    arms = read_armor_data('ARM')
    waists = read_armor_data('WAIST')
    legs = read_armor_data('LEG')
    eligible_heads = [head for head in heads if head.is_eligible(search_criteria)]
    eligible_chests = [chest for chest in chests if chest.is_eligible(search_criteria)]
    eligible_arms = [arm for arm in arms if arm.is_eligible(search_criteria)]
    eligible_waists = [waist for waist in waists if waist.is_eligible(search_criteria)]
    eligible_legs = [leg for leg in legs if leg.is_eligible(search_criteria)]

    # generate permutations
    possible_combination_count = len(eligible_heads) * len(eligible_chests) * len(eligible_arms) * len(eligible_waists) * len(eligible_legs)
    combinations_generator = itertools.product(eligible_heads, eligible_chests, eligible_arms, eligible_waists, eligible_legs)
    print(f'permutations: {possible_combination_count}')

    # process permutations
    count = 0
    results = []
    for index, combination in zip(range(possible_combination_count), combinations_generator):
        helm, mail, braces, coil, greaves = combination
        result = Result(helm, mail, braces, coil, greaves)
        if result.matches_search_criteria(search_criteria):
            results.append(result)
            count += 1

        if count >= 10:
            break

        progress_bar(index + 1, possible_combination_count)

    # present results
    results.sort(key=lambda r: r.get_defense())    
    print('\n')
    for result in results:
        print(result)
    
    end = time.time()
    length = end - start
    print(f'matches: {count}')
    print('time:', length, 'seconds')

def progress_bar(iteration, total, length = 50):
    progress = int(length * iteration / total)
    bar = '=' * progress + '-' * (length - progress)
    percent = 100 * iteration / total

    sys.stdout.write(f'\r[{bar}] {percent:.2f}% Complete')
    sys.stdout.flush()

def read_armor_data(type):
    with open('armor.json', 'r') as file:
        data = json.load(file)
        armors = []
        for item in data:
            if item['type'] == type:
                armor = Armor(
                    item['name'],
                    item['type'],
                    item['defense'],
                    item['fireRes'],
                    item['waterRes'],
                    item['thunderRes'],
                    item['iceRes'],
                    item['dragonRes'],
                    item['slot1'],
                    item['slot2'],
                    item['slot3'],
                    item.get('groupSkill'),
                    item.get('skill1'),
                    item.get('skillLevel1'),
                    item.get('skill2'),
                    item.get('skillLevel2'),
                    item.get('skill3'),
                    item.get('skillLevel3')
                )
                armors.append(armor)

        return armors

if __name__ == '__main__':
    sys.exit(main())
