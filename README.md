# DFT_files

Collection of python scripts to write Gaussian/Orca DFT input files from xyz coordinates (to be finished) and to parse DFT output files (to be added)

## xyz_to_com.py 

This script is to be placed into the same folder as where the xyz files are stored.
This folder should also contain a template.com template gaussian input file with the details of the Gaussian job (but without any coordinates).
The first line of this template.com file should contain: %chk=name.chk

The scripts uses the template.com file to generate new .com files of the same name as the initial .xyz files and replaces "name.chk" with the name of the xyz file to generate the corresponding .chk file with the correct naming. It appends the xyz coordinates after the last written line of the template.com file
