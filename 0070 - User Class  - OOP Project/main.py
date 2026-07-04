import sys
from user import User

u = None
for raw in sys.stdin.read().split('\n'):
    line = raw.strip()
    if not line:
        continue
    parts = line.split()
    cmd = parts[0]
    if cmd == 'new':
        u = User(parts[1], parts[2])
    if cmd == 'username':
        print(u.username)
    if cmd == 'email':
        print(u.email)
    if cmd == 'setLocation':
        u.setLocation(parts[1])
    if cmd == 'getLocation':
        print(u.getLocation())
    if cmd == 'info':
        u.info()
    if cmd == 'learn':
        u.learn(parts[1])
    if cmd == 'showSkills':
        u.showSkills()
    if cmd == 'clearSkill':
        u.clearSkill(parts[1])
    if cmd == 'calculateSalary':
        print(u.calculateSalary())
