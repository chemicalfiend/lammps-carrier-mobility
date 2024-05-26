"""

Generates input files for Gaussian transfer integral calculations.

"""


import os

num_molecules = 10
atoms_per_mol = 324

class Atom:
    def __init__(self, n, mol, typeid, charge, x, y, z):
        self.n = n
        self.mol = mol
        self.charge = charge
        self.x = x
        self.y = y
        self.z = z

        if(typeid <= 18):
            self.atomtype = "C"

        elif(typeid > 18 and typeid <= 31):
            self.atomtype = "H"

        elif(typeid == 32):
            self.atomtype = "F"
        
        elif(typeid == 33):
            self.atomtype = "Cl"

        elif(typeid == 34):
            self.atomtype = "Br"

        elif(typeid == 35):
            self.atomtype = "I"

        elif(typeid >= 36 and typeid <= 56):
            self.atomtype = "N"

        elif(typeid >= 57 and typeid <= 62):
            self.atomtype = "O"

        elif (typeid >= 63 and typeid <= 73):
            self.atomtype = "P"

        elif (typeid >= 74 and typeid <= 83):
            self.atomtype = "S"

        else:
            self.atomtype = " "
"""
class Bond:
    def __init__(self, a1, a2):
        self.atom1 = a1
        self.atom2 = a2
"""

fc = open("sorted_coords.data", "r") 

clines = fc.readlines()

line_count = 1

for mol in range(1, num_molecules):
    with open(f"monomers/K1tenmols_mol_{mol}.dat", "w") as fout:
        for j in range(1, atoms_per_mol):
            line = clines[line_count]
            tokens = line.split()
            #print(tokens)    
            n = int(tokens[0])
            m = int(tokens[1])
            typeid = int(tokens[2])
            charge = float(tokens[3])
            x = float(tokens[4])
            y = float(tokens[5])
            z = float(tokens[6])
            line_count += 1
            
            fout.writeline("{typeid} \t {x} \t {y} \t {z} \n")


