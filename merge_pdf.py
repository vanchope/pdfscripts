#!/bin/python3
# TODO customize output name
# TODO spaces in filenames?
from tkinter import messagebox as mbox
from tkinter import Tk
import os
import traceback
import subprocess, shlex

TITLE = "Pdf Merger"
root = Tk()
root.withdraw()
try:
    input_files = os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS'].splitlines()
    basedirs = set([os.path.dirname(f) for f in input_files])
    if len(basedirs)!=1:
        mbox.showerror(TITLE,'expected files from the same directory')
    else:
        basedir = basedirs.pop()
        input_filenames = [os.path.basename(f) for f in input_files]
        input_files_line = '\n'.join(input_filenames)
        output_filename = 'OUT.pdf'
        answer = mbox.askokcancel(TITLE, f"Merge pdf files in '{basedir}' directory this order\n\n {input_files_line}\n\n and output to {output_filename}. Is this what you want?")
        if answer:
            output_file = os.path.join(basedir, 'OUT.pdf')
            proceed = True
            if os.path.isfile(output_file):
                proceed = mbox.askyesno(TITLE, f"File {output_file} exists. Overwrite?")
            if proceed:
                input_files_satinized = ['"' + f + '"' for f in input_files]
                cmd = f'pdftk {" ".join(input_files_satinized)} cat output {output_file}'
                subprocess.Popen(shlex.split(cmd))
except Exception as err:
    mbox.showerror(TITLE, traceback.format_exc())