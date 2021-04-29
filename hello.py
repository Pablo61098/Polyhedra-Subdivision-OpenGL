import glfw
from OpenGL.GL import  *
import numpy as np


def main():
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Hello World", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.set_window_pos(window, 540, 350)

    # Make the window's context current
    glfw.make_context_current(window)

    vertices = [-0.5, -0.5, 0.0,
                0.4, -0.5, 0.0,
                1.0, 0.5, 1.0]

    colors = [1.0, 0.0, 0.0,
                0.0, 1.0, 1.0,
                2.0, 0.0, 0.0]

    vertices = np.array(vertices, dtype=np.float32)
    colors = np.array(colors, dtype=np.float32)

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(3, GL_FLOAT, 0, colors)

    glClearColor(0.1, 0.1, 0.1, 0.4)

    # Loop until the user closes the window
    rotate = 1
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL

        # Swap front and back buffers
        glfw.swap_buffers(window)

        glClear(GL_COLOR_BUFFER_BIT)

        glRotate(rotate, 0, 1, 0)
        
        #  rotate += 1

        glDrawArrays(GL_TRIANGLES, 0, 3)
        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()