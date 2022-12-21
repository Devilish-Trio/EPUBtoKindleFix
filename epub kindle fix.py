import os
import subprocess 
import tkinter as tk  
import time  
from tkinter import filedialog 

def select_input_file(input_format):
    """
    Display a file dialog to select the input file.
    
    Parameters:
    input_format (str): The format of the input file (e.g. 'epub', 'mobi')
    
    Returns:
    str: The path to the selected input file
    """
    # Create a root window and withdraw it (i.e. hide it)
    root = tk.Tk()
    root.withdraw()

    # Display the file dialog to select the input file
    input_file = filedialog.askopenfilename(
        parent=root,
        title=f'Select input {input_format} file',  # Set the dialog title based on the input format
        filetypes=[(f'{input_format.upper()} files', f'*.{input_format}')]  # Set the allowed file types based on the input format
    )

    return input_file

def convert_ebook(input_file, output_file, output_format):
    """
    Convert an ebook from one format to another using ebook-convert.
    
    Parameters:
    input_file (str): The path to the input ebook file
    output_file (str): The path to the output ebook file
    output_format (str): The format of the output ebook file (e.g. 'epub', 'mobi')
    """
    cmd = ['ebook-convert', input_file, output_file]  # Set up the ebook-convert command
    subprocess.run(cmd)  # Run the ebook-convert command

# Select the input epub file
input_format = 'epub'
input_file = select_input_file(input_format)

# Convert the input epub file to output.mobi
convert_ebook(input_file, 'output.mobi', 'mobi')

# Wait for 1 second
time.sleep(1)

# Convert output.mobi back to output.epub
convert_ebook('output.mobi', 'output.epub', 'epub')

# Delete the output.mobi file
os.remove('output.mobi')
