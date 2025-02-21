import random

class Result:
    def __init__(self, helm, mail, braces, coil, greaves):
        self.helm = helm
        self.mail = mail
        self.braces = braces
        self.coil = coil
        self.greaves = greaves

    def __repr__(self):
        return f"{self.get_defense()}: {self.helm.name}, {self.mail.name}, {self.braces.name}, {self.coil.name}, {self.greaves.name}"

    def get_defense(self):
        return self.helm.defense + self.mail.defense + self.braces.defense + self.coil.defense + self.greaves.defense

    def get_combined_skills(self):
        noncombined_skills = self.helm.skills + self.mail.skills + self.braces.skills + self.coil.skills + self.greaves.skills

        aggregated = {}
        for item in noncombined_skills:
            name = item["name"]
            level = item["level"]
            if name in aggregated:
                aggregated[name] += level
            else:
                aggregated[name] = level

        return aggregated
    
    def matches_search_criteria(self, search_criteria):
        combined_skills = self.get_combined_skills()

        for skill in search_criteria.skills:
            search_criteria_skill_name = skill['name']
            if search_criteria_skill_name not in combined_skills:
                return False

            skill_level = combined_skills[skill['name']]
            if skill_level < skill['level']:
                return False

        return True
