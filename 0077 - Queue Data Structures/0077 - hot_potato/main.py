from solution import hotPotato
import sys

lines = sys.stdin.read().split("\n")
names = lines[0].split()
tosses = int(lines[1])
print(hotPotato(names, tosses))
