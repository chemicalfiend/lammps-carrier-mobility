cstart = 94 # line number where coords start (-1)
cend = 144894 # line number where coords end

filepath = "final.data"


fd = open(filepath, "r")
fo = open("sorted_coords.data", "w")

lines = fd.readlines()

atoms = []

for i in range(cstart, cend):
    line = lines[i]
    tokens = line.split()
    n = int(tokens[0])
    mol = int(tokens[1])
    typeid = int(tokens[2])
    charge = float(tokens[3])
    x = float(tokens[4])
    y = float(tokens[5])
    z = float(tokens[6])
    if (mol <= 200):
        atoms.append((n, mol, typeid, charge, x, y, z))


atoms.sort(key = lambda a: a[0])

for a in atoms:
    fo.write(f"{a[0]} {a[1]} {a[2]} {a[3]} {a[4]} {a[5]} {a[6]} \n")

fd.close()
fo.close()



