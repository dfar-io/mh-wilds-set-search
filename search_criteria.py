class SearchCriteria:
    def __init__(self, skills, rank):
        self.skills = skills
        self.rank = rank

    def __repr__(self):
        return (
            f'criteria:\n'
            f'skills: {self.skills}\n'
            f'rank: {self.rank}\n'
        )
