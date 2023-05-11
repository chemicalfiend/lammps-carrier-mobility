import numpy as np

from morphct.system import System
from morphct.mobility_kmc import snap_molecule_indices
from morphct.chromophores import amber_dict

import gsd.hoomd


from bbl_dict import bbl_dict

gsdfile = "trajectory.gsd"

with gsd.hoomd.open(name=gsdfile, mode='rb') as f:
    snap = f[-1]


#print(snap.particles.types[snap.particles.typeid[175]])

print(snap.particles.typeid)
print(snap.particles.types)

gsd_mol_index = snap_molecule_indices(snap)
k = np.count_nonzero(gsd_mol_index==0)
chromo_ids = np.arange(snap.particles.N)[0:k]


master_list = []
sublist = chromo_ids
for i in range(len(np.unique(gsd_mol_index))):        
    master_list.append(sublist)
    sublist = np.array([x + k for x in sublist])


#print(master_list)
if __name__ == '__main__':
    system = System(gsdfile, "y6", frame=-1, scale=3.5636, conversion_dict=bbl_dict)
    system.add_chromophores(master_list,"acceptor")
    system.compute_energies()
    system.set_energies()
    lifetime = [1e-10,1e-9]
    temp = 300
    system.run_kmc(lifetime, temp, n_elec =1000)




