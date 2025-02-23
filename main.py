import json
import sys
from armor import Armor
from result import Result
from search_criteria import SearchCriteria
import itertools
import time

search_criteria = SearchCriteria([
    { 'Quick Sheathe': 2 },
    { 'Focus' : 3 }
], 1)

def main():
    start = time.time()

    print(search_criteria)

    # load data
    heads = read_armor_data('head.json')
    chests = read_armor_data('chest.json')
    arms = read_armor_data('arms.json')
    waists = read_armor_data('waist.json')
    legs = read_armor_data('legs.json')
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
        if count > 200:
            print ("limit reached")
            break
        result = Result(helm, mail, braces, coil, greaves)
        if result.matches_search_criteria(search_criteria):
            results.append(result)
            count += 1

        progress_bar(index + 1, possible_combination_count)

    # present results
    results.sort(key=lambda r: r.get_defense())    
    print('\n')
    for result in results:
        print(result)
    
    end = time.time()
    length = end - start
    print("Process time:", length, "seconds")

def progress_bar(iteration, total, length = 50):
    progress = int(length * iteration / total)
    bar = '=' * progress + '-' * (length - progress)
    percent = 100 * iteration / total
    sys.stdout.write(f'\r[{bar}] {percent:.2f}% Complete')
    sys.stdout.flush()

def read_armor_data(json_filename):
    with open(json_filename, 'r') as file:
        data = json.load(file)
        return [Armor(
            item["name"],
            item['rank'],
            item["baseDefense"],
            item["slots"],
            item["fireResistance"],
            item["waterResistance"],
            item["thunderResistance"],
            item["iceResistance"],
            item["dragonResistance"],
            item["skills"]
        ) for item in data]

if __name__ == '__main__':
    sys.exit(main())
