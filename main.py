import sys
import tkinter as tk
from clock import Clock

# https://www.w3schools.com/charsets/ref_html_utf8.asp
# to use UTF-8 symbols: chr uses dec representation and \u hex representation
START_TEXT = ">" # chr(9655) # "\u25B6"
STOP_TEXT = "O"  # chr(9633) # "\u25A0"
CLOSE_TEXT = "X" # "\u2715"

class StopWatch(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.clock = Clock()
        self.counter_clock = Clock()
        self.with_seconds = False
        self.display = 1

        self.timestr = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_display = tk.Label(self, textvariable=self.timestr)
        self.lbl_display.pack(side=tk.LEFT)
        self.lbl_display.bind('<Double-Button-1>', self.reset)
        self.lbl_display.bind('<Button-4>', self.add)
        self.lbl_display.bind('<Button-5>', self.substract)
        self.lbl_display.bind('<Button-3>', self.alternate_displays)
        # self.lbl_display.bind('<Double-Button-3>', self.toggle_show_seconds)
        # self.lbl_display.bind('<MouseWheel>', self.add) # windows
        self.update_label()

        self.btn_start_stop = tk.Button(
            self, text=START_TEXT, padx=5, pady=0, command=self.start_stop
        )
        self.btn_start_stop.pack(side=tk.LEFT)
        self.btn_start_stop.bind('<Button-3>', self.toggle_show_seconds)

        self.btn_close = tk.Button(
            self, text=CLOSE_TEXT, padx=5, pady=0, command=quit
        )
        self.btn_close.pack(side=tk.LEFT)

        # self.toggle_show_seconds(None) # uncomment for easier testing


    ## Event handlers

    def start_stop(self):
        if self.clock.running:
            self.clock.stop()
            self.counter_clock.start()
            self.cancel_refresh_loop()
            self.btn_start_stop.config(text=START_TEXT)
        else:
            self.clock.start()
            self.counter_clock.stop()
            self.refresh_loop()
            self.btn_start_stop.config(text=STOP_TEXT)

    def substract(self, event):
        self.clock.move(-300)
        self.counter_clock.move(300)
        self.update_label()

    def add(self, event):
        self.clock.move(300)
        self.counter_clock.move(-300)
        self.update_label()
    
    def reset(self, event):
        if self.clock.running:
            self.cancel_refresh_loop()
            self.btn_start_stop.config(text=START_TEXT)
        self.clock.reset()
        self.counter_clock.reset()
        self.update_label()

    def toggle_show_seconds(self, event):
        self.with_seconds = not self.with_seconds
        if self.clock.running:
            self.cancel_refresh_loop()
            self.refresh_loop()
        else:
            self.update_label()

    def alternate_displays(self, event):
        self.display += 1
        if self.display >= 4:
            self.display = 1
        self.update_label()

    ## Helper methods

    def refresh_loop(self):
        self.update_label()
        self.refresh_loop_reference = self.after(
            self.refresh_interval(), self.refresh_loop
        )

    def cancel_refresh_loop(self):
        if not hasattr(self, 'refresh_loop_reference'):
            return
        self.after_cancel(self.refresh_loop_reference)

    def update_label(self):
        if self.display == 1:
            self.timestr.set(self.display_time(self.clock.elapsed_time()))
        elif self.display == 2:
            self.timestr.set('L ' + self.display_time(self.clock.elapsed_time_since_last_stop()))
        elif self.display == 3:
            self.timestr.set('C ' + self.display_time(self.counter_clock.elapsed_time()))
        else:
            raise RuntimeError('Display number is wrong')

    def refresh_interval(self):
        return 1000 if self.with_seconds else 60000 # in milisec

    def display_time(self, time_in_seconds):
        sign = '-' if time_in_seconds < 0 else ''
        time_in_seconds = abs(time_in_seconds)
        hours = time_in_seconds // 3600
        minutes = (time_in_seconds - hours * 3600) // 60
        result = '%s%02d:%02d' % (sign, hours, minutes)
        if self.with_seconds:
            seconds = time_in_seconds - (hours * 3600 + minutes * 60)
            result += ':%02d' % seconds
        return result


def main():
    root = tk.Tk()
    #root.title("SW")
    
    ## Remove this section to create normal window
    root.overrideredirect(True)
    root.wm_attributes('-topmost', True)

    sw = StopWatch(root)
    sw.pack(side=tk.TOP)

    if len(sys.argv) == 3:
        sw.position = (int(sys.argv[1]), int(sys.argv[2]))
    else:
        ## Position the window in the center
        sw.position = (root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2)
    root.geometry('+%d+%d' % sw.position)

    ## Adds capability to move window clicking on frame
    def moving(event):
        sw.position = (event.x_root, event.y_root)
        root.geometry("+%s+%s" % sw.position)
    sw.lbl_display.bind("<B1-Motion>", moving)
    sw.btn_close.bind('<Button-3>', lambda event: sw.timestr.set("%s, %s" % sw.position))

    ## Mainloop
    root.mainloop()

if __name__ == '__main__':
    main()
