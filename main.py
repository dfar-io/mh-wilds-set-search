import json
import sys
from armor import Armor
from result import Result
import itertools

def progress_bar(iteration, total, length = 50):
    progress = int(length * iteration / total)
    bar = '=' * progress + '-' * (length - progress)
    percent = 100 * iteration / total
    sys.stdout.write(f'\r[{bar}] {percent:.2f}% Complete')
    sys.stdout.flush()

def main():
    with open('helms.json', 'r') as file:
        helmData = json.load(file)
        helms = [Armor(item["name"], item["baseDefense"], item["skills"], item['rank']) for item in helmData]
    with open('mails.json', 'r') as file:
        mailData = json.load(file)
        mails = [Armor(item["name"], item["baseDefense"], item["skills"], item['rank']) for item in mailData]
    with open('braces.json', 'r') as file:
        braceData = json.load(file)
        braces = [Armor(item["name"], item["baseDefense"], item["skills"], item['rank']) for item in braceData]
    with open('coils.json', 'r') as file:
        coilData = json.load(file)
        coils = [Armor(item["name"], item["baseDefense"], item["skills"], item['rank']) for item in coilData]
    with open('greaves.json', 'r') as file:
        greaveData = json.load(file)
        greaves = [Armor(item["name"], item["baseDefense"], item["skills"], item['rank']) for item in greaveData]

    search_criteria = [
        { 'name': 'Attack Boost', 'level': 7 },
        { 'name': 'Critical Eye', 'level': 7 },
        { 'name': 'Weakness Exploit', 'level': 3 }
    ]
    search_criteria_skill_names = [item["name"] for item in search_criteria]

    eligible_helms = [helm for helm in helms if helm.is_eligible(search_criteria_skill_names)]
    eligible_mails = [mail for mail in mails if mail.is_eligible(search_criteria_skill_names)]
    eligible_braces = [brace for brace in braces if brace.is_eligible(search_criteria_skill_names)]
    eligible_coils = [coil for coil in coils if coil.is_eligible(search_criteria_skill_names)]
    eligible_greaves = [greave for greave in greaves if greave.is_eligible(search_criteria_skill_names)]
    possible_combination_count = len(eligible_helms) * len(eligible_mails) * len(eligible_braces) * len(eligible_coils) * len(eligible_greaves)

    combinations_generator = itertools.product(eligible_helms, eligible_mails, eligible_braces, eligible_coils, eligible_greaves)
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

if __name__ == '__main__':
    sys.exit(main())

