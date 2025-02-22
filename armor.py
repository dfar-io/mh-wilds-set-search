class Armor:
    def __init__(self, name, defense, skills, rank):
        self.name = name
        self.defense = defense
        self.skills = skills
        self.rank = rank
    
    def is_eligible(self, search_criteria):
        if self.rank != search_criteria.rank:
            return False

        search_criteria_skill_names = [item["name"] for item in search_criteria.skills]
        skill_names = [item["name"] for item in self.skills]
        common_elements = set(skill_names) & set(search_criteria_skill_names)
        
        return len(common_elements) > 0
