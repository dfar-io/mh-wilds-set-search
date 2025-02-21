import json
import sys
from armor import Armor
from result import Result
import itertools

def is_eligible(armor):
    print(type(armor))
    armor_skills = armor['skills']
    armor_skill_names = [item['name'] for item in armor_skills]
    common_elements = set(armor_skill_names) & set(search_criteria_skill_names)

    return common_elements.length > 0

def main():
    with open('helms.json', 'r') as file:
        helmData = json.load(file)
        helms = [Armor(item["name"], item["baseDefense"], item["skills"]) for item in helmData]
    with open('mails.json', 'r') as file:
        mailData = json.load(file)
        mails = [Armor(item["name"], item["baseDefense"], item["skills"]) for item in mailData]
    with open('braces.json', 'r') as file:
        braceData = json.load(file)
        braces = [Armor(item["name"], item["baseDefense"], item["skills"]) for item in braceData]
    with open('coils.json', 'r') as file:
        coilData = json.load(file)
        coils = [Armor(item["name"], item["baseDefense"], item["skills"]) for item in coilData]
    with open('greaves.json', 'r') as file:
        greaveData = json.load(file)
        greaves = [Armor(item["name"], item["baseDefense"], item["skills"]) for item in greaveData]

    search_criteria = [
        { 'name': 'Attack Boost', 'level': 3 },
        { 'name': 'Critical Eye', 'level': 7 },
        { 'name': 'Critical Boost', 'level': 7 },
        { 'name': 'Weakness Exploit', 'level': 7 },
        { 'name': 'Focus', 'level': 7 },
        { 'name': 'Quick Sheathe', 'level': 7 },
        { 'name': 'Critical Draw', 'level': 7 }
    ]
    search_criteria_skill_names = [item["name"] for item in search_criteria]

    eligible_helms = [helm for helm in helms if helm.is_eligible(search_criteria_skill_names)]
    eligible_mails = [mail for mail in mails if mail.is_eligible(search_criteria_skill_names)]
    eligible_braces = [brace for brace in braces if brace.is_eligible(search_criteria_skill_names)]
    eligible_coils = [coil for coil in coils if coil.is_eligible(search_criteria_skill_names)]
    eligible_greaves = [greave for greave in greaves if greave.is_eligible(search_criteria_skill_names)]

    combinations_generator = itertools.product(eligible_helms, eligible_mails, eligible_braces, eligible_coils, eligible_greaves)
    count = 0
    for combination in combinations_generator:
        helm, mail, braces, coil, greaves = combination
        if count > 10000:
            print ("limit reached")
            break
        result = Result(helm, mail, braces, coil, greaves)
        if result.matches_search_criteria(search_criteria):
            print(result)
            count += 1

if __name__ == '__main__':
    sys.exit(main())

