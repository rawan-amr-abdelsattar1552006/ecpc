n = int(input())
smurfs = []

for i in range(n):
    smurf = input().count("1")
    smurfs.append(smurf)

if len(list(set(smurfs))) == 1:
    print(2)
    
else:
    win = smurfs.count(max(smurfs))
    print(win)
