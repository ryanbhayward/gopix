# convert gdg-crds to gdg-plain 
import sys

L = sys.stdin.readlines()
E = []
for k in range(len(L)): 
  entries = L[k].split()
  for j in range(len(entries)):
    ej = entries[j]
    if ej.isnumeric():
      entries[j] = 'o' if int(ej)%2 == 0 else 'x'
  E.append(entries)
for e in E:
  print((' ').join(e))
