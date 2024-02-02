# lammps-carrier-mobility
Workflow for getting the carrier mobilities from LAMMPS trajectories.

To run this workflow, you need to install and build the package MorphCT (https://github.com/cmelab/morphct), along with mBuild and gsd, which you can get by simply using conda-forge.

## Using the script

Dump the relevant snapshot from your LAMMPS trajectory as a LAMMPS data file. Extract the coordinates and bonds and sort them by their index number and save them as "sorted\_coords.data" and "sorted\_bonds.data" respectively.

Activate a conda environment in which you have mbuild and gsd installed and then run the following command:

```
python3 gsdwriter.py

```

This will convert the sorted\_coords and sorted\_bonds files into a gsd file called "system.gsd". Then you can run any kmc code based off of this. A sample kmc workflow is provided in kmc-script.py. The md-example directory showcases this being used for a system with 10 PEDOT molecules.


