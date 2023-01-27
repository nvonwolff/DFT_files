#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:54:34 2023

@author: niklas
"""
import os

template_file = "template.inp"
folder = os.path.dirname(os.path.abspath(__file__))

# Iterate through .xyz files in folder
for file in os.listdir(folder):
    if file.endswith(".xyz"):
        # Open template file and read all lines
        with open(template_file, "r") as f:
            template_lines = f.readlines()

        # Get the name of the .xyz file without the extension
        xyz_name = os.path.splitext(file)[0]

        # Open .xyz file and read coordinates
        with open(os.path.join(folder, file), "r") as f:
            coordinates = f.readlines()[2:]

        # find the last non-empty line in the template file
        last_line = len(template_lines) - 1
        while last_line >= 0:
            if template_lines[last_line].strip():
                break
            last_line -= 1

        # Append xyz coordinates after the last non-empty line of the template file
        template_lines = template_lines[:last_line + 1] + coordinates + [' *\n']

        # Create new .inp file with name of .xyz file
        new_file = xyz_name + ".inp"
        with open(os.path.join(folder, new_file), "w") as f:
            # Write all lines to new file
            f.writelines(template_lines)



