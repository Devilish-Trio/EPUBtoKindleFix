import subprocess
import tkinter as tk
from tkinter import filedialog

def epub_to_mobi(mobi_file):
    root = tk.Tk()
    root.withdraw()

    epub_file = filedialog.askopenfilename(
        parent=root,
        title='Select input epub file',
        filetypes=[('EPUB files', '*.epub')]
    )

    cmd = ['ebook-convert', epub_file, mobi_file]
    subprocess.run(cmd)

epub_to_mobi('output.mobi')

def mobi_to_epub(epub_file):
    root = tk.Tk()
    root.withdraw()

    mobi_file = filedialog.askopenfilename(
        parent=root,
        title='Select input mobi file',
        filetypes=[('MOBI files', '*.mobi')]
    )

    cmd = ['ebook-convert', mobi_file, epub_file]
    subprocess.run(cmd)

mobi_to_epub('output.epub')