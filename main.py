import json
import sys
from armor import Armor
from result import Result
from search_criteria import SearchCriteria
import itertools
import time

def progress_bar(iteration, total, length = 50):
    progress = int(length * iteration / total)
    bar = '=' * progress + '-' * (length - progress)
    percent = 100 * iteration / total
    sys.stdout.write(f'\r[{bar}] {percent:.2f}% Complete')
    sys.stdout.flush()

def main():
    start = time.time()

    with open('head.json', 'r') as file:
        headData = json.load(file)
        heads = [Armor(item["name"], item["baseDefense"], item["skills"], item['rank']) for item in headData]
    with open('chest.json', 'r') as file:
        chestData = json.load(file)
        chests = [Armor(item["name"], item["baseDefense"], item["skills"], item['rank']) for item in chestData]
    with open('arms.json', 'r') as file:
        armsData = json.load(file)
        arms = [Armor(item["name"], item["baseDefense"], item["skills"], item['rank']) for item in armsData]
    with open('waist.json', 'r') as file:
        waistData = json.load(file)
        waists = [Armor(item["name"], item["baseDefense"], item["skills"], item['rank']) for item in waistData]
    with open('legs.json', 'r') as file:
        legsData = json.load(file)
        legs = [Armor(item["name"], item["baseDefense"], item["skills"], item['rank']) for item in legsData]

    search_criteria = SearchCriteria([
        { 'name': 'Quick Sheathe', 'level': 3 },
        { 'name': 'Focus', 'level': 3 }
    ], 1)

    eligible_heads = [head for head in heads if head.is_eligible(search_criteria)]
    eligible_chests = [chest for chest in chests if chest.is_eligible(search_criteria)]
    eligible_arms = [arm for arm in arms if arm.is_eligible(search_criteria)]
    eligible_waists = [waist for waist in waists if waist.is_eligible(search_criteria)]
    eligible_legs = [leg for leg in legs if leg.is_eligible(search_criteria)]
    possible_combination_count = len(eligible_heads) * len(eligible_chests) * len(eligible_arms) * len(eligible_waists) * len(eligible_legs)

    combinations_generator = itertools.product(eligible_heads, eligible_chests, eligible_arms, eligible_waists, eligible_legs)
    count = 0
    results = []
    print(f'possible combos: {possible_combination_count}')
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

    results.sort(key=lambda r: r.get_defense())
    for result in results:
        print(result)
        print(result.get_combined_skills())
        print()

    end = time.time()
    length = end - start
    print()
    print("Process time:", length, "seconds")

if __name__ == '__main__':
    sys.exit(main())

