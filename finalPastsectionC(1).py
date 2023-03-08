student = [
    ["111","A",76,98,67,83],
    ["222","B",67,84,84,56],
    ["333","C",92,83,69,72],
    ["444","D",82,76,68,82],
    ["555","E",56,63,72,53]
]

print("""
                    LIST OF STUDENT AND MARK        
ID\tNAME\tBM\tBI\tMATH\tSCI\tTOTAL\tAVERAGE
----------------------------------------------------------------------------""")
for i in range(0,len(student)):
    total = sum(student[i][2:])
    for j in range(0,len(student[i])):
        avg = total/len(student[i][2:])
        print(student[i][j],end="\t")
    print(total,"\t",avg)


