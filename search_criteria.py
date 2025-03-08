class SearchCriteria:
    def __init__(self, skills):
        self.skills = skills

    def __repr__(self):
        return (
            f'criteria:\n'
            f'skills: {self.skills}\n'
        )
