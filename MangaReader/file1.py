import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import time

# Functions
start_time = time.time()
stop_time = 5

def welcome_display():

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
    

        if elapsed_time < stop_time:
            welcome_image = Image.open(r"frontend/imageAssetsGenerate/UI_UX-assets/a_WelcomeDisplay.png")
            w_image = tk.PhotoImage(welcome_image)
            w = tk.Label(image=w_image)
            w.pack()

        else:
            w.destroy()
        

def load_info_page():
    filem = filedialog.askopenfilename()
    pass

def load_folder(): # same
    pass

def nav_to_viewer(): # same
    pass

def next_image():
    pass

def previous_image():
    pass

def zoom_out():
    pass

def zoom_in():
    pass

def exit_zoom():
    pass

def back_to_info_page():
    pass

def update_recent_reads():
    pass


# welcome_label = tk.Label()

root = tk.Tk()

root.title("eMANHWA") # The name of the code is printed at the bar.
root.state("zoomed") # The default state of the program is full screen mode
root.iconphoto(False, tk.PhotoImage(file="frontend/imageAssetsGenerate/UI_UX-assets/eMr.png"))

""" info_frame = tk.Frame()

selection_frame = tk.Frame()
selection_label = tk.Label() # Select manhwa header text
selection_button = tk.Button()

history_label = tk.Label()
history_text = tk.Label() # recent reads header text

viewer_frame = tk.Frame()

manhwa_label = tk.Label()

exit_viewer_button_image = tk.PhotoImage(file="frontend/imageAssetsGenerate/UI_UX-assets/exit_viewer_button.png")
exit_viewer_button = tk.Button()

next_button_image = tk.PhotoImage(file="frontend/imageAssetsGenerate/UI_UX-assets/rightbut.png")
next_button = tk.Button()

previous_button_image = tk.PhotoImage(file="frontend/imageAssetsGenerate/UI_UX-assets/leftbut.png")
previous_button = tk.Button()

"""

welcome_display()

root.mainloop()
