import guilib as gl
"""
Goal: A program that draws a figure, and reports the x and y data values of the clicked point.
"""
state = {
    "textbox": None,
    "points": []
}

def choose_point(event):
    """
    Receives a mouse event from a mouse click and reads the x and y data 
    values from it. The values are printed into a textbox, and saved to a list
    in the program's state dictionary.
    """
    
    gl.write_to_textbox(
    state["textbox"],
    "Value at x={:.2f} is {:.2f}".format(event.xdata, event.ydata)
    )
    point = event.xdata, event.ydata
    state["points"].append(point)
    print(state["points"])

    
def main(x, y):
    """
    Creates a user interface that contains an interactive figure and a textbox.
    A plot based on data received as parameters is drawn into the figure.
    """ 
    testwindow = gl.create_window("pointing_is_rude")
    figureframe = gl.create_frame(testwindow, gl.TOP)
    textbox = gl.create_frame(testwindow, gl.BOTTOM)
    fig = gl.create_figure(figureframe, choose_point, 600, 400)
    state["textbox"] = gl.create_textbox(textbox)
    fig[0].draw()
    fig[2].plot(x, y)
    gl.start()

if __name__ == "__main__":
    datax = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    datay = [0.0, 0.19, 0.36, 0.51, 0.64, 0.75, 0.84, 0.91, 0.96, 0.99, 1.0, 0.99, 0.96, 0.91, 0.84, 0.75, 0.64, 0.51, 0.36, 0.19, 0.0]
    main(datax, datay)