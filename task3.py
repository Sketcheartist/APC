

import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

files = []

def select_files():
    global files
    files = list(filedialog.askopenfilenames(
        filetypes=[("PDF Files", "*.pdf")]))
    file_list.delete(0, tk.END)
    for f in files:
        file_list.insert(tk.END, f)

def merge_pdfs():
    if len(files) < 2:
        messagebox.showerror("Error", "Select at least 2 PDFs")
        return
    output = filedialog.asksaveasfilename(
        defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
    if output:
        merger = PdfMerger()
        try:
            for f in files:
                merger.append(f)
            merger.write(output)
            messagebox.showinfo("Success", "PDFs merged successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            merger.close()

def clear_files():
    global files
    files = []
    file_list.delete(0, tk.END)

root = tk.Tk()
root.title("PDF Merger")
root.geometry("550x400")

tk.Label(root, text="PDF Merger Application",
         font=("Arial", 18, "bold")).pack(pady=10)

file_list = tk.Listbox(root, width=70, height=12)
file_list.pack(pady=10)

tk.Button(root, text="Select Files", command=select_files,
          width=15).pack(pady=5)
tk.Button(root, text="Merge", command=merge_pdfs,
          width=15, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Clear", command=clear_files,
          width=15, bg="lightcoral").pack(pady=5)

root.mainloop()
