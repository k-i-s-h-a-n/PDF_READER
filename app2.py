import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import filedialog

def read_specific_page(reading_pdf, page_entry):
    try:
        page_number = int(page_entry.get()) - 1  # Subtract 1 to match 0-based index
        chosen_page = reading_pdf.pages[page_number]
        pdf_text = chosen_page.extract_text()

        pdf_speaker = pyttsx3.init()
        voices = pdf_speaker.getProperty('voices')
        voice_id = 'english-us'
        pdf_speaker.setProperty('voice', voice_id)
        current_rate = pdf_speaker.getProperty('rate')
        pdf_speaker.setProperty('rate', 125)
        pdf_speaker.say(pdf_text)
        pdf_speaker.runAndWait()
        pdf_speaker.setProperty('rate', current_rate)
    except ValueError:
        pass  

def read_pdf():
    def open_pdf():
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        
        if file_path:
            pdf_book = open(file_path, 'rb')
            reading_pdf = PyPDF2.PdfReader(pdf_book)

            page_frame = tk.Toplevel(root)
            page_frame.title("Select Page")

            page_label = tk.Label(page_frame, text="Enter Page Number:")
            page_label.pack(side=tk.LEFT)

            page_entry = tk.Entry(page_frame)
            page_entry.pack(side=tk.LEFT)

            read_button = tk.Button(page_frame, text="Read Page", command=lambda: read_specific_page(reading_pdf, page_entry))
            read_button.pack(side=tk.LEFT)

    root = tk.Tk()
    root.title("PDF Reader")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=30)

    browse_button = tk.Button(frame, text="READ PDF", command=open_pdf)
    browse_button.pack(padx=10, pady=10)

    root.mainloop()

read_pdf()
