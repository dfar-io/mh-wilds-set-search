class Armor:
    def __init__(self, name, defense, skills, rank):
        self.name = name
        self.defense = defense
        self.skills = skills
        self.rank = rank
    
    def is_eligible(self, search_criteria_skill_names):
        skill_names = [item["name"] for item in self.skills]
        common_elements = set(skill_names) & set(search_criteria_skill_names)
        print(self.rank)
        
        return len(common_elements) > 0 or self.rank == 2
