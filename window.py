from tkinter import *

main_window = Tk()
main_window.title("Sound Wave Analysis")
main_window.geometry("1800x800")



#labels





#buttons
load_file = Button(main_window, text="Load file") # add, command = load
load_file.pack(side = "left", padx = (700,50))


combine_plots = Button(main_window, text="Combine plots") # add, command = combine
combine_plots.pack(side = "left")



alternate_plots1 = Button(main_window, text="Alternate plots") # extra credit, add, command = alternate_plots, alternates between low, mid, high plots
alternate_plots1.pack(side = "left", padx = 50)


#add button and additional visual output (our choice)


main_window.mainloop()