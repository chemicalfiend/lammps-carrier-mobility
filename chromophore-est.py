from copy import deepcopy
import numpy as np


from morphct.system import System
from morphct.mobility_kmc import snap_molecule_indices


from bbl_dict2 import bbl_dict

import gsd.hoomd
import pickle

fname = "neutral.gsd"
sysname = "neutral"

with gsd.hoomd.open(name=fname, mode='rb') as f:
    snap = f[-1]


print(*snap.particles.typeid)
print(snap.particles.types)

print(snap.particles.types[snap.particles.typeid[7]])


box = snap.configuration.box[:3]
# ref_distance should convert the distances into angstroms. This number can likey be
# in the directory of your MD simulations
ref_distance = 3.563594872561358
unwrapped_positions = snap.particles.position + snap.particles.image * box
snap.particles.position *= ref_distance
snap.configuration.box[:3] *= ref_distance
unwrap_snap = deepcopy(snap)
unwrap_snap.particles.position = unwrapped_positions
unwrap_snap.particles.types = [bbl_dict[i].symbol for i in snap.particles.types]


gsd_mol_index = snap_molecule_indices(snap)
print(gsd_mol_index)
k = np.count_nonzero(gsd_mol_index==0)
chromo_ids = np.arange(snap.particles.N)[0:k]


master_list = []
sublist = chromo_ids

for i in range(len(np.unique(gsd_mol_index))):
    master_list.append(sublist)
    sublist = np.array([x + k for x in sublist])


if __name__ == '__main__':
    system = System(fname, sysname, frame=-1, scale=3.5636, conversion_dict=bbl_dict)
    system.add_chromophores(master_list, "acceptor", chromophore_kwargs={"reorganization_energy" : 0.324})
    system.compute_energies()
    system.set_energies()
    picklename = sysname + "-est.pickle"
    system_pickle = open(picklename,'wb')
    pickle.dump(system, system_pickle)
    system_pickle.close()

    


