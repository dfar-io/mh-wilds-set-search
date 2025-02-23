class SearchCriteria:
    def __init__(self, rank, skills, min_slots):
        self.rank = rank
        self.skills = skills
        self.min_slots = min_slots

    def __repr__(self):
        return (
            f'criteria:\n'
            f'skills: {self.skills}\n'
            f'rank: {self.rank}\n'
            f'min_slots: {self.min_slots}\n'
        )
