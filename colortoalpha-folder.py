#!/usr/bin/env python

from gimpfu import *
import os, os.path


# our script
def open_fix_save (target_file, target_color):
    pdb = gimp.pdb
    try:
        image = pdb.gimp_file_load(target_file, target_file)
        drawable = pdb.gimp_image_get_active_drawable(image)
        try:
            pdb.plug_in_colortoalpha(image, drawable, target_color)
            try:
                pdb.file_png_save_defaults(image, drawable, target_file, target_file)
                pdb.gimp_image_delete(image)
            except:
                pass
        except:
            pass
    except:
        pass

def colortoalpha_folder(target_folder, target_color) :
    for root, subFolders, files in os.walk(str(target_folder)):
        for file in files:
            fname = file
            if not os.path.isdir(fname):
                open_fix_save(os.path.join(root, fname), target_color)
    return

# This is the plugin registration function
register(
    "colortoalpha-folder",    
    "Convert a specified color to transparency across multiple files in a folder",   
    "Uses Seth Burgess's colortoalpha plugin across multiple files: 'This replaces as much of a given color as possible in each pixel with a corresponding amount of alpha, then readjusts the color accordingly.'",
    "Nic West", 
    "STUNJELLY", 
    "June 2012",
    "<Toolbox>/Scripts/Multiple Color to Alpha", 
    "", 
    [
      (PF_FILE, 'target_folder', 'Target Folder', '/'),
      (PF_COLOR, 'target_color', 'Color to Alpha', '#FFFFFF'),
    ], 
    [],
    colortoalpha_folder,
    )

main()