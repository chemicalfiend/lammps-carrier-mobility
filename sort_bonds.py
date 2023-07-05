cstart = 457599 # line number where coords start (-1)
cend = 687159 # line number where coords end

fd = open("final-10.data", "r")
fo = open("sorted_bonds.data", "w")

rs = 1      # Index for start of relevant molecules
re = 200    # Index for end of relevant molecules

atoms = 324 # Atoms per molecule

totalAtoms = 324 * (re - rs + 1)

lines = fd.readlines()

bonds = []

for i in range(cstart, cend):
   # print(i)
    line = lines[i]
    tokens = line.split()
    n = int(tokens[0])
    typ = int(tokens[1])
    a1 = int(tokens[2])
    a2 = int(tokens[3])
    
    if(a1 <= totalAtoms and a2 <= totalAtoms):
        bonds.append((n, typ, a1, a2))

bonds.sort(key = lambda b: b[2])

for b in bonds:
    fo.write(f"{b[0]} {b[1]} {b[2]} {b[3]} \n")

fd.close()
fo.close()



