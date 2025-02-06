import tkinter as tk
import time
import random

# Lists of rotating content
equations = [
    "E = hf", "Δx Δp ≥ ℏ/2", "Ψ(x,t) = Ae^{i(kx - \\omega t)}",
    "iℏ ∂Ψ/∂t = ĤΨ", "E_n = -13.6 eV / n^2", "J = L - S", "σ_x σ_y - σ_y σ_x = 2iσ_z"
]
greek_political_parties = ["ND", "SYRIZA", "KKE", "PASOK", "MERA25", "Elliniki Lysi"]
greek_philosophers = ["Socrates", "Plato", "Aristotle", "Epicurus", "Heraclitus", "Pythagoras"]
metal_albums = ["Master of Puppets", "Paranoid", "The Number of the Beast", "Reign in Blood", "Rust in Peace", "Black Album"]
movies_directors = ["Kubrick - 2001: A Space Odyssey", "Tarantino - Pulp Fiction", "Nolan - Inception", "Scorsese - Goodfellas", "Spielberg - Jaws", "Coppola - The Godfather"]

# Function to update clocks
def update_clock():
    current_time = time.strftime("%H:%M")
    time_label.config(text=current_time)
    root.after(1000, update_clock)

# Function to update rotating texts every minute
def update_texts():
    equation_label.config(text=random.choice(equations))
    party_label.config(text=random.choice(greek_political_parties))
    philosopher_label.config(text=random.choice(greek_philosophers))
    album_label.config(text=random.choice(metal_albums))
    movie_label.config(text=random.choice(movies_directors))
    root.after(60000, update_texts)

# Create main window
root = tk.Tk()
root.title("Rotating Quantum, Politics, Philosophy, Metal, and Movies Clock")
root.geometry("600x500")
root.configure(bg='black')

# Time display
time_label = tk.Label(root, font=("Courier", 40, "bold"), fg="cyan", bg="black")
time_label.pack(pady=10)

# Rotating text displays
equation_label = tk.Label(root, font=("Courier", 16), fg="yellow", bg="black")
equation_label.pack()
party_label = tk.Label(root, font=("Courier", 16), fg="red", bg="black")
party_label.pack()
philosopher_label = tk.Label(root, font=("Courier", 16), fg="green", bg="black")
philosopher_label.pack()
album_label = tk.Label(root, font=("Courier", 16), fg="blue", bg="black")
album_label.pack()
movie_label = tk.Label(root, font=("Courier", 16), fg="magenta", bg="black")
movie_label.pack()

# Start updating the clock and texts
update_clock()
update_texts()

# Run the application
root.mainloop()
