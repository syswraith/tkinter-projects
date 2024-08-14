import tkinter as tk
import ttkbootstrap as ttk

# convert function
def convert(): output_str.set(float(entry_int.get()) * 1.6)

# window
window = ttk.Window(themename="darkly")
window.title("Demo")
window.geometry("500x300")

# title
title_label = ttk.Label(master = window, text = "Miles to kilometers", font = "Calibri 24 bold")
title_label.pack(pady =(75, 0))

# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# output
output_str = tk.StringVar()
output_label = ttk.Label(
	master = window, 
	text = "Placeholder", 
	font = "Calibri 20", 
	textvariable=output_str
)
output_label.pack(pady=5)

# run 
window.mainloop()
