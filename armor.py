class Armor:
    def __init__(self, name, rank, defense, slots, fire, water, thunder, ice, dragon, skills):
        self.name = name
        self.rank = rank
        self.defense = defense
        self.slots = slots
        self.fire = fire
        self.water = water
        self.thunder = thunder
        self.ice = ice
        self.dragon = dragon
        self.skills = skills
    
    def is_eligible(self, search_criteria):
        if self.rank != search_criteria.rank:
            return False

        search_criteria_skill_names = set(key for d in search_criteria.skills for key in d.keys())
        skill_names = [item['name'] for item in self.skills]
        common_skills = set(skill_names) & set(search_criteria_skill_names)
        
        return len(common_skills) > 0
    
    def get_slot(self, slot):
        return self.slots[slot] if 0 <= slot < len(self.slots) else 0