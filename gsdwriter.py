"""

Program to write a GSD file for a trajectory from a LAMMPS data file.

Used for Charge Transport calculations

"""


import mbuild as mb
import numpy as np
import os
import networkx as nx


num_molecules = 200
atoms_per_mol = 324


if(os.path.exists("systemdmbi1.gsd")):
    os.remove("systemdmbi1.gsd")
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

bonds = []

for line in blines:
    tokens = line.split()
    #print(tokens)
    atom1 = int(tokens[2])
    atom2 = int(tokens[3])

    bonds.append((atom1-1, atom2-1))

graph = nx.Graph()

for bond in bonds:
    graph.add_edge(bond[0], bond[1])

#for i in range(392):
#    print(bonds[i])

status = []
for i in range(0, n): status.append(False)

compounds = []

system = mb.Compound()

#for i in range(num_molecules):

count = 0

#print(len(atoms))

for c in nx.connected_components(graph):
    mol = mb.Compound()
    
    temp = list(c)
    temp.sort()
    #print(temp)
    for item in temp:
        #print(item)
        atom = atoms[item]

        mol.add(mb.Particle(pos=[atom.x, atom.y, atom.z], element = atom.atomtype, name=atom.atomtype, charge= atom.charge))
        #system.add(mb.Particle(pos=[atom.x, atom.y, atom.z], element = atom.atomtype, name=atom.atomtype, charge= atom.charge))

        status[item] = True

    #for bond in bonds:
    #    mol.add_bond((bond[0]-1, bond[1]-1))
    for edge in graph.subgraph(c).edges:
        #print(edge)
        mol.add_bond((mol[edge[0]-((atoms_per_mol)*count)], mol[edge[1]-((atoms_per_mol)*count)]))
        #system.add_bond((system[edge[0]], system[edge[1]]))
    
    compounds.append(mol)
    count = count + 1

"""
for atom in atoms:
    system.add(mb.Particle(pos=[atom.x, atom.y, atom.z], element = atom.atomtype, name=atom.atomtype, charge= atom.charge))

    particle_list = list(system.children)

for bond in bonds:
    if atoms[bond[0]].mol == m:
        system.add_bond((particle_list[bond[0]], particle_list[bond[1]]))


"""
system.add(compounds)

print(system.n_bonds)

system.save("systemdmbi1.gsd")
