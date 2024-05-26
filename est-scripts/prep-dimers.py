"""

Program to write a GSD file for a trajectory from a LAMMPS data file.

Used for Charge Transport calculations

"""


import mbuild as mb
import numpy as np
import os
import networkx as nx
import freud

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

class Bond:
    def __init__(self, a1, a2):
        self.atom1 = a1
        self.atom2 = a2


fc = open("sorted_coords.data", "r")
fb = open("sorted_bonds.data", "r")

clines = fc.readlines()
blines = fb.readlines()

atoms = []

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


status = []
for i in range(0, n): status.append(False)

compounds = []

system = mb.Compound()

centers = []

count = 0
for c in nx.connected_components(graph):
    mol = mb.Compound()
    
    temp = list(c)
    temp.sort()
    
    molnum = count + 1
    fout = open(f"monomers/K1tenmols_mol_{molnum}.dat", "w")

    for item in temp:
        atom = atoms[item]

        mol.add(mb.Particle(pos=[atom.x, atom.y, atom.z], element = atom.atomtype, name=atom.atomtype, charge= atom.charge))

        fout.write(f"{atom.atomtype} \t {atom.x} \t {atom.y} \t {atom.z} \n")
            

        status[item] = True

    for edge in graph.subgraph(c).edges:
        mol.add_bond((mol[edge[0]-((atoms_per_mol)*count)], mol[edge[1]-((atoms_per_mol)*count)]))
    
    centers.append(mol.center)
    compounds.append(mol)
    count = count + 1
    fout.close()



system.add(compounds)

voronoi = freud.locality.Voronoi()
freudbox = freud.box.Box.from_box(system.get_boundingbox())
voronoi.compute((freudbox, centers))

neighbours = []

for (i, j) in voronoi.nlist:
    if i == j:
        pass

    elif (i, j) not in neighbours and (j, i) not in neighbours:
        neighbours.append((i, j))


for (i, j) in neighbours:
    i1 = i + 1
    j1 = j + 1
    
    
    fd = open(f"dimers/K1tenmols_dim_{i1}_{j1}.dat", "w")
    
    fi = open(f"monomers/K1tenmols_mol_{i1}.dat", "r")
    fj = open(f"monomers/K1tenmols_mol_{j1}.dat", "r")

    for line in fi.readlines():
        fd.write(line)


    for line in fj.readlines():
        fd.write(line)

    fi.close()
    fj.close()
    fd.close()
