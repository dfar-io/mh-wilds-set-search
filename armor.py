class Armor:
    def __init__(self, name, rarity, defense, slots, fire, water, thunder, ice, dragon, skills):
        self.name = name
        self.rarity = rarity
        self.defense = defense
        self.slots = slots
        self.fire = fire
        self.water = water
        self.thunder = thunder
        self.ice = ice
        self.dragon = dragon
        self.skills = skills
        
    
    def is_eligible(self, search_criteria):
        search_criteria_skill_names = [item["name"] for item in search_criteria.skills]
        skill_names = [item["name"] for item in self.skills]
        common_elements = set(skill_names) & set(search_criteria_skill_names)
        
        return len(common_elements) > 0
