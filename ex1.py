import tkinter as tk
 # Create the main Tkinter window
parent = tk.Tk()
parent.title("Vertical Labels with Pack")
 # Create three label widgets
label1 = tk.Label(parent, text="Python Exercises", padx=10, pady=5)
label2 = tk.Label(parent, text="Java Exercises", padx=10, pady=5)
label3 = tk.Label(parent, text="C++ Exercises", padx=10, pady=5)
 # Use the Pack geometry manager to arrange labels vertically
label1.pack(side="top")
label2.pack(side="top")
label3.pack(side="top")
 # Run the Tkinter main loop
parent.mainloop()
