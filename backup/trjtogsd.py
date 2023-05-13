#import planckton

import mdtraj as md
import mbuild as mb
#import gsd
#from planckton.init import Compound

#tr = md.load_lammpstrj('mol.lammpstrj', top='alt.pdb')

system = mb.load("data.mol2")

#system = mb.load(tr)

system.box = mb.Box([200.0, 200.0, 200.0])

#system.translate([77.0, 77.0, 29.0])

system.save("traj3.gsd")



