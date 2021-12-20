"""
Prints a test line into a textbox in the user interface.
"""
import guilib as gl
LEFT = gl.LEFT
RIGHT = gl.RIGHT
TOP = gl.TOP
BOTTOM = gl.BOTTOM


widgets = {
    "textbox": None
    }
def print_testline():
    gl.write_to_textbox(widgets["textbox"], "hoho")
    
"""
Creates an application window with two buttons on the left and one textbox on
the right. Text can be printed to the box by pressing a button.
"""
def main():
    
    testwindow = gl.create_window("test window")
    buttonframe = gl.create_frame(testwindow, LEFT)
    textbox = gl.create_frame(testwindow, RIGHT)
    gl.create_button(buttonframe, "test", print_testline)
    gl.create_button(buttonframe, "quit", gl.quit)
    widgets["textbox"] = gl.create_textbox(textbox, 34, 20)
    gl.start()
    
if __name__ == "__main__": 
    main()