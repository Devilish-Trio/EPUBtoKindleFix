import subprocess
import tkinter as tk
import time
from tkinter import filedialog

def select_input_file(input_format):
    root = tk.Tk()
    root.withdraw()

    input_file = filedialog.askopenfilename(
        parent=root,
        title=f'Select input {input_format} file',
        filetypes=[(f'{input_format.upper()} files', f'*.{input_format}')]
    )

    return input_file

def convert_ebook(input_file, output_file, output_format):
    cmd = ['ebook-convert', input_file, output_file]
    subprocess.run(cmd)

# Select input epub file
input_format = 'epub'
input_file = select_input_file(input_format)

# Convert input epub to output.mobi
convert_ebook(input_file, 'output.mobi', 'mobi')

# Wait for 1 second
time.sleep(1)

# Convert output.mobi back to output.epub
convert_ebook('output.mobi', 'output.epub', 'epub')
