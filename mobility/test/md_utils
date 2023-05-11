import mdtraj as md
import mbuild as mb
import gsd


tr = md.load_lammpstrj('trajectory.lammpstrj', top='data.pdb')
system = mb.load(tr)

system.save("trajectory.gsd")



