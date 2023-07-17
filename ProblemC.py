n,a,b = [int(x) for x in input().split(" ")]
teams = list(input())

count = 0
count_e = 0

for team in teams:
    if team == "S" and count < a + b:
        count += 1
        print("Yes")
        
    elif team == "E" and count < a + b and count_e < b:
        
        count_e += 1
        count += 1
        
        print("Yes")
        
    elif team == "U":
        print("No")
        
    else:
        print("No")
