import tkinter as tk
from tkinter import filedialog
import PyPDF2

def get_metadata():
    # Öffnen Sie ein Dialogfenster, um eine PDF-Datei auszuwählen
    filepath = filedialog.askopenfilename(filetypes=[("PDF Dateien", "*.pdf")])
    if not filepath:
        return

    # Öffnen Sie die PDF-Datei und lesen Sie die Metadaten
    with open(filepath, "rb") as file:
        pdf = PyPDF2.PdfFileReader(file)
        metadata = pdf.getDocumentInfo()
       

    # Erstellen Sie einen Textbereich, um die Metadaten anzuzeigen
    text = tk.Text(root)
    text.pack()
    text.insert("end", "Metadaten:\n")
    for key, value in metadata.items():
        text.insert("end", f"{key}: {value}\n")
        
        

# Erstellen Sie die Hauptfenster-GUI
root = tk.Tk()
root.title("PDF Metadata Viewer - created by RevInsp Sasha SESLIJA")

# Erstellen Sie eine Schaltfläche, um die Metadaten abzurufen
button = tk.Button(root, text="Wählen Sie eine PDF-Datei aus", command=get_metadata)
button.pack()

root.mainloop()
