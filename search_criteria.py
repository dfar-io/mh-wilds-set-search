class SearchCriteria:
    def __init__(self, skills, min_slots):
        self.skills = skills
        self.min_slots = min_slots

    def __repr__(self):
        return (
            f'criteria:\n'
            f'skills: {self.skills}\n'
            f'min level 1 slots: {self.min_slots[0]}\n'
            f'min level 2 slots: {self.min_slots[1]}\n'
            f'min level 3 slots: {self.min_slots[2]}\n'
        )
