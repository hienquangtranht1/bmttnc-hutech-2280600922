input_str=input("Nhập X,Y: ")
diemsions=[int(x) for x in input_str.split(",")]
rowNum=diemsions[0]
colNun=diemsions[1]
multilist = [[0 for i in range(colNun)] for j in range(rowNum)]
for row in range(rowNum):
    for col in range(colNun):
        multilist[row][col] = row * col
print(multilist)