class Result:
    def __init__(self, head, chest, arms, waist, legs):
        self.head = head
        self.chest = chest
        self.arms = arms
        self.waist = waist
        self.legs = legs

    def __repr__(self):
        return (
            f'{self.get_defense()}: {self.head.name}, {self.chest.name}, {self.arms.name}, {self.waist.name}, {self.legs.name}\n'
            f'{self.get_combined_skills()}\n'
            f'F: {self.head.fire} W: {self.head.water} T: {self.head.thunder} I: {self.head.ice} D: {self.head.dragon}\n'
        )

    def get_defense(self):
        return self.head.defense + self.chest.defense + self.arms.defense + self.waist.defense + self.legs.defense

    def get_combined_skills(self):
        noncombined_skills = self.head.get_skills() + self.chest.get_skills() + self.arms.get_skills() + self.waist.get_skills() + self.legs.get_skills()

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
            search_criteria_skill_name = list(skill)[0]
            if search_criteria_skill_name not in combined_skills:
                return False

            skill_level = combined_skills[search_criteria_skill_name]
            if skill_level < skill[search_criteria_skill_name]:
                return False

        return True
