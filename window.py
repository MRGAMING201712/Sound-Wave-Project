from tkinter import *

main_window = Tk()
main_window.title("Sound Wave Analysis")
main_window.geometry("1800x800")

# Load file button
load_file = Button(main_window, text="Load file")  # Add command=load if needed
load_file.place(x=900, y=50)

# Intensity graph, Wave graph, and Alternate plots buttons next to each other

intensity_graph = Button(main_window, text="Intensity graph")
intensity_graph.place(x=780, y=500)

wave_graph = Button(main_window, text="Wave graph")
wave_graph.place(x=900, y=500)

alternate_plots = Button(main_window, text="Alternate plots")  # Add command=combine if needed
alternate_plots.place(x=1000, y=500)


# Combine plots button below Alternate plots buttons
combine_plots = Button(main_window, text="Combine plots")  # Add command=alternate_plots for extra credit
combine_plots.place(x=1000, y=550)

# Run the main loop
main_window.mainloop()
