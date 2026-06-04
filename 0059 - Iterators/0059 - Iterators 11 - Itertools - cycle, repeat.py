print("****** CYCLE *******************************")
from itertools import cycle

szerverlista = ["szerver1", "szerver2", "szerver3"]
forgalomiranyito = cycle(szerverlista)
for i in range(7):
    print(next(forgalomiranyito))

print("****** REPEAT   *******************************")
from itertools import repeat

for cimke in repeat("Made in Japan", 5):
    print(cimke)


