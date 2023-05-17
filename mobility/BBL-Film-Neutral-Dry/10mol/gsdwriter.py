"""

Program to write a GSD file for a trajectory from a LAMMPS data file.

Used for Charge Transport calculations

"""


import mbuild as mb
import numpy as np
import os

num_molecules = 10
atoms_per_mol = 324


if(os.path.exists("system.gsd")):
    os.remove("system.gsd")
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

        elif(typeid >= 36 and typeid <= 48):
            self.atomtype = "N"

        elif(typeid >= 49 and typeid <= 52):
            self.atomtype = "O"

        elif (typeid >= 53 and typeid <= 63):
            self.atomtype = "P"

        elif (typeid >= 64 and typeid <= 71):
            self.atomtype = "S"

        else:
            self.atomtype = " "

class Bond:
    def __init__(self, a1, a2):
        self.atom1 = a1
        self.atom2 = a2


fc = open("sorted_coords.data", "r")
fb = open("sorted_bonds.data", "r")

clines = fc.readlines()
blines = fb.readlines()

atoms = []

"""
xlo = float(lines[13].split()[0])
xhi = float(lines[13].split()[1])
ylo = float(lines[14].split()[0])
yhi = float(lines[14].split()[1])
zlo = float(lines[15].split()[0])
zhi = float(lines[15].split()[1])
"""

# TODO : Manually set the box coordinates.


for line in clines:
    tokens = line.split()
    #print(tokens)    
    n = int(tokens[0])
    mol = int(tokens[1])
    typeid = int(tokens[2])
    charge = float(tokens[3])
    x = float(tokens[4])
    y = float(tokens[5])
    z = float(tokens[6])
    
    atoms.append(Atom(n, mol, typeid, charge, x, y, z))

# Store and add bonds

# TODO: Read and store charges of individual atoms

bondi = []
bondj = []

for line in blines:
    tokens = line.split()
    #print(tokens)
    atom1 = int(tokens[2])
    atom2 = int(tokens[3])

    bondi.append(atom1)
    bondj.append(atom2)

#print(bondi)
#print(bondj)
system = mb.Compound()

# System box and other parameters set.

#system.box = mb.Box([xhi-xlo, yhi-ylo, zhi-zlo])


for i in range(num_molecules):
    m = i + 1
    mol = mb.Compound()

    for atom in atoms:
        if atom.mol == m:
            a = mb.Particle(pos=[atom.x, atom.y, atom.z], element = atom.atomtype, name=atom.atomtype, charge= atom.charge)
            mol.add(a)

    system.add(mol)


for i in range(len(bondi)):
    #print(f"Adding bond number {i}")
    system.add_bond((system[bondi[i] - 1], system[bondj[i] - 1]))


print(system.n_bonds)

system.save("system.gsd")
