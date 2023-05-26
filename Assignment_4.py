#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 4

import tkinter as tk

# Create the main root
root = tk.Tk()
root.title("2 Labels with different background colors:")
root.geometry("600x500")

# Create the first label with a blue background
label1 = tk.Label(root, text="Label 1", bg="pink", fg="red")
label1.pack(fill = tk.BOTH, expand = True)


# Create the second label with a green background
label2 = tk.Label(root, text="Label 2", bg="black", fg="white")
label2.pack(fill = tk.BOTH, expand = True)


# Start the Tkinter event loop
root.mainloop()

