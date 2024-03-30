import customtkinter as tk

root = tk.CTk()
root.title("Category Sort")
root.geometry("500x500")

catSelectFrame = tk.CTkFrame(root,width=50)
catSelectFrame.grid(row=1,column=1)
catSearchBarWidgets = tk.CTkFrame(master=catSelectFrame)
catSearchBarWidgets.pack()
catSearchOutputFrame = tk.CTkScrollableFrame(catSelectFrame,height=200)
catSearchOutputFrame.pack()

materialOutputFrame = tk.CTkFrame(root)
materialOutputFrame.grid(row=1,column=2)
matSearchBarWidgets = tk.CTkFrame(master=materialOutputFrame)
matSearchBarWidgets.pack()