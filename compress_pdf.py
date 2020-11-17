#!/bin/python3
# TODO customize output name
# TODO check if outputfile exists
# TODO spaces in filenames?
from tkinter import messagebox as mbox
from tkinter import Tk
import os
import traceback
import subprocess, shlex

TITLE = "Pdf Tools"
COMPRESSION = "ebook"  # ebook | printer
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
        answer = mbox.askokcancel(TITLE, f"Compress pdf file(s)\n\n {input_files_line}\n\n and save output with a suffix '.c.pdf'. Is this what you want?")
        if answer:
            for input_file in input_files:
                if input_file.endswith('.pdf'):
                    output_file = input_file[:-4] + ".c.pdf"
                else:
                    output_file = input_file + ".c.pdf"
                # option "-sColorConversionStrategy=Gray"
                cmd=f'gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/{COMPRESSION} -dNOPAUSE -dQUIET -dBATCH -sOutputFile="{output_file}" "{input_file}"'
                subprocess.Popen(shlex.split(cmd))
except Exception as err:
    mbox.showerror(TITLE, traceback.format_exc())