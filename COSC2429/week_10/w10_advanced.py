class School:
    target = 0.99

    def __init__(self, capital):
        self.budget = capital

    def max_expenditure(self):
        return self.budget * School.target


print(School.target)
s = School(100000)
print(s.budget)
print(s.max_expenditure())