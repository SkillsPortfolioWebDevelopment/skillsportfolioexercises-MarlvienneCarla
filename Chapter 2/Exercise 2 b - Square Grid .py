import tkinter as tk

#create the main window
window = tk.Tk()
window.title("Label Layout with Pack")

#create two frames for layout
left_frame = tk.Frame(window, borderwidth=2, relief="solid")
right_frame = tk.Frame(window, borderwidth=2, relief="solid")

#pack frames to the lest and right of the window
left_frame.pack(side="left", fill="both", expand=True)
right_frame.pack(side="right", fill="both", expand=True)

#create label for the left frame
label_a = tk.Label(left_frame, text="A", bg="#131E3A")
label_c = tk.Label(left_frame, text="B", bg="white", fg="black")
label_a.pack(side="top", fill="both", expand=True)
label_c.pack(side="top", fill="both", expand=True)

#create labels fo rthe right frame
label_b = tk.Label(right_frame, text="C", bg="#131E3A")
label_d = tk.Label(right_frame, text="D", bg="white", fg="black")
label_b.pack(side="bottom", fill="both", expand=True)
label_d.pack(side="bottom", fill="both", expand=True)

window.mainloop()
