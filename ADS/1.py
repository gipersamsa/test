import tkinter as tk
wind = tk.Tk()

text = tk.Label(text="Name",width = 25,height = 2)
name = tk.Entry(width = 25)
text1 = tk.Label(text="Username",width = 25,height = 2)
username = tk.Entry(width = 50)
text2 = tk.Label(text="Age",width = 25,height = 2)
age = tk.Entry(width = 75)
greeting = tk.Label(width = 100, height = 2, fg = "yellow", bg = "black")

greeting.pack()
text.pack()
name.pack()
text1.pack()
username.pack()
text2.pack()
age.pack()

wind.mainloop()