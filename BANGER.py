import tkinter as tk
import random
import time
import threading
import os

# ====== SOUND (funguje jen na Windows) ======
def beep():
    try:
        import winsound
        winsound.Beep(1000, 100)
    except:
        pass

# ====== APP ======
root = tk.Tk()
root.title("CYBERPUNK TASK SYSTEM")
root.geometry("500x600")
root.configure(bg="black")

# ====== CLOCK ======
clock_label = tk.Label(root, font=("Courier", 16), fg="lime", bg="black")
clock_label.pack()

def update_clock():
    now = time.strftime("%H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)

update_clock()

# ====== TITLE ======
title = tk.Label(root, text=">> SYSTEM ONLINE <<", font=("Courier", 18, "bold"), fg="cyan", bg="black")
title.pack(pady=10)

# ====== ANIMACE TEXTU ======
glitch_texts = ["HACKING...", "ACCESS GRANTED", "OVERRIDE", "ENCRYPTING", "DECRYPTING"]
glitch_label = tk.Label(root, font=("Courier", 12), fg="magenta", bg="black")
glitch_label.pack()

def animate_text():
    glitch_label.config(text=random.choice(glitch_texts))
    root.after(500, animate_text)

animate_text()

# ====== INPUT ======
entry = tk.Entry(root, font=("Courier", 14), bg="black", fg="lime", insertbackground="lime")
entry.pack(pady=10)

# ====== LIST ======
listbox = tk.Listbox(root, font=("Courier", 12), bg="black", fg="white", selectbackground="lime")
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# ====== FUNCTIONS ======
def add_task(event=None):
    task = entry.get()
    if task:
        listbox.insert(tk.END, f"> {task}")
        entry.delete(0, tk.END)
        beep()

def delete_task(event=None):
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        pass

def clear_all():
    listbox.delete(0, tk.END)

# ====== BUTTONS ======
frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

add_btn = tk.Button(frame, text="ADD", command=add_task, fg="black", bg="lime")
add_btn.grid(row=0, column=0, padx=5)

del_btn = tk.Button(frame, text="DELETE", command=delete_task, fg="black", bg="red")
del_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(frame, text="CLEAR ALL", command=clear_all, fg="black", bg="yellow")
clear_btn.grid(row=0, column=2, padx=5)

# ====== KEYBINDS ======
root.bind("<Return>", add_task)
root.bind("<Delete>", delete_task)

# ====== RANDOM BACKGROUND FLASH ======
def flash_bg():
    colors = ["black", "#050505", "#0a0a0a"]
    root.configure(bg=random.choice(colors))
    root.after(200, flash_bg)

flash_bg()

# ====== START ======
root.mainloop()