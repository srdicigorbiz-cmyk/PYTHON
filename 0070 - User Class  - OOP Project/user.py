class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.location = 'unset'
        self.skills = {}

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def info(self):
        print(f'Username: {self.username}')
        print(f'Email: {self.email}')
        print(f'Location: {self.location}')

    def learn(self, skill):
        if skill not in self.skills:
            self.skills[skill] = 0
        self.skills[skill] += 1

    def showSkills(self):
        for key in sorted(self.skills.keys()):
            print(f'{key}: {self.skills[key]}')

    def clearSkill(self, skill):
        if skill in self.skills:
            del self.skills[skill]

    def calculateSalary(self):
        # TODO: Write code here
        sum_of_all_skill_levels = 0
        for s in self.skills:
            sum_of_all_skill_levels += self.skills[s]
        return sum_of_all_skill_levels * 100
