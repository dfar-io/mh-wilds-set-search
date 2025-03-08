class Armor:
    def __init__(self, name, type, defense, fire, water, thunder, ice, dragon, slot1, slot2, slot3, group_skill, skill_1, skill_1_level, skill_2, skill_2_level, skill_3, skill_3_level):
        self.name = name
        self.type = type
        self.defense = defense
        self.fire = fire
        self.water = water
        self.thunder = thunder
        self.ice = ice
        self.dragon = dragon
        self.slot1 = slot1
        self.slot2 = slot2
        self.slot3 = slot3
        self.group_skill = group_skill
        self.skill_1 = skill_1
        self.skill_1_level = skill_1_level
        self.skill_2 = skill_2
        self.skill_2_level = skill_2_level
        self.skill_3 = skill_3
        self.skill_3_level = skill_3_level
    
    def is_eligible(self, search_criteria):
        print(self.get_skills())

        search_criteria_skill_names = set(key for d in search_criteria.skills for key in d.keys())
        skill_names = [item['name'] for item in self.get_skills()]
        common_skills = set(skill_names) & set(search_criteria_skill_names)
        
        return len(common_skills) > 0
    
    def get_skills(self):
        result = []
        if self.skill_1 != None:
            result.append({ 'name': self.skill_1, 'level': self.skill_1_level })
        if self.skill_2 != None:
            result.append({ 'name': self.skill_2, 'level': self.skill_2_level })
        if self.skill_3 != None:
            result.append({ 'name': self.skill_3, 'level': self.skill_3_level })

        return result