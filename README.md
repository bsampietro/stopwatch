# Stopwatch
Very simple and small stopwatch. Runs always on top. Made with Python and tkinter.

## Run it
$ python3 route/to/main.py [x-position y-position]

### Linux
Needs to have tkinter library available. tkinter is part of standard libray but tk-dev system package 
needs to be available when compiling Python from source.

If using system Python, need to install python-tk package.

Only tested on Linux, probably works on other platforms too with minor changes.

## Functions
Reset: Double-click on label.

Add or substract 5 minutes: Mouse wheel on label.

Toggle L view and C view: Right click on play button. L view shows time since last stop. C shows total time the clock was stopped since it was started from a reset.

Show seconds: Right click on play button.

Window position coordinates: Left click on close button (remove by clicking start/stop). Useful for knowing the position in order to pass x-position and y-position when starting it.
