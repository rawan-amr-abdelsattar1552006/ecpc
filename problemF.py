n = int(input())
smurfs = []

for i in range(n):
    smurf = input().count("1")
    smurfs.append(smurf)

if len(list(set(smurfs))) == 1 and n % 2 == 0:
    print(n)
elif len(list(set(smurfs))) == 1 and n % 2 != 0:
    print(n - 1)
else:
    win = smurfs.count(max(smurfs))
    print(win)
