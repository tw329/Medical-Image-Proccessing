l = []
l2 = [1, 10]
l.append(12)
l2 = [10, 100]
l.append(12)
l2 = [20, 200]
l.append(12)

rows = 3;
cols = 2;

for i in range(0, rows):
    for j in range(0, cols):
        print(l[i][j])
        print(" ")
    print("\n")