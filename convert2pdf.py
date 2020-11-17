#!/bin/python3
# TODO check if outputfile exists
from tkinter import messagebox as mbox
from tkinter import Tk
import os
import traceback
import subprocess, shlex

TITLE = "Pdf Tools"
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
        input_files_line = ', '.join(input_filenames)
        output_filename = 'OUT.pdf'
        answer = mbox.askokcancel(TITLE, f"Convert file(s)\n\n {input_files_line}\n\n to pdf with a suffix '.pdf'. Is this what you want?")
        if answer:
            for input_file in input_files:
                output_file = input_file + ".pdf"
                cmd=f'convert "{input_file}" "{output_file}"'
                subprocess.Popen(shlex.split(cmd))
except Exception as err:
    mbox.showerror(TITLE, traceback.format_exc())