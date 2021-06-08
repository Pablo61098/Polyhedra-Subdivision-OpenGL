import glfw
from OpenGL.GL import  *
import numpy as np
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr
from subdivide import update_figure
from figures import define_figure
import time
import argparse

start_time = time.time()


vertex_src = """
# version 330 core

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_color;

out vec3 v_color;

uniform mat4 rotation;

void main()
{
        gl_Position = rotation * vec4(a_position, 1.0);
        v_color = a_color;
}
"""

fragment_src = """
# version 330 core


in vec3 v_color;
out vec4 out_color;

void main()
{
    out_color = vec4(v_color, 1.0);
}
"""

def get_new_figure(vertices_array, indices_array, vertices, indices, flag, norm):
    vertices_array, indices_array = update_figure(vertices_array, indices_array, norm)

    vertices = np.array(vertices_array, dtype=np.float32)
    indices = np.array(indices_array, dtype=np.uint32)

    glBufferSubData(GL_ARRAY_BUFFER, 0, 4*len(vertices)+32, vertices)

    
    glBufferSubData(GL_ELEMENT_ARRAY_BUFFER, 0, 4*len(vertices)+32, indices)
    

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(12))


    return vertices_array, indices_array, vertices, indices


def window_resize(window, width, height):
    glViewport(0, 0, width, height)

def main(figure, norm):
   
    
    if not glfw.init():
        return
   
    window = glfw.create_window(1024, 1024, "Subdivisión de Poliedros", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.set_window_pos(window, 400, 200)

    glfw.set_window_size_callback(window, window_resize)

   
    glfw.make_context_current(window)

    vertices_array, indices_array = define_figure(figure)
    

    indices = np.array(indices_array, dtype=np.uint32)

    vertices = np.array(vertices_array, dtype=np.float32)

    shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

    VBO = glGenBuffers(1)
   
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER,  1000000000, None, GL_STATIC_DRAW)
    glBufferSubData(GL_ARRAY_BUFFER, 0, 4*len(vertices), vertices)
    

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 1000000000, None, GL_STATIC_DRAW)
    glBufferSubData(GL_ELEMENT_ARRAY_BUFFER, 0, 4*len(indices), indices)

   
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
   
    

   
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(12))


    glUseProgram(shader)
    glClearColor(0, 0.1, 0.1, 1)
    glEnable(GL_DEPTH_TEST)

    rotation_loc = glGetUniformLocation(shader, "rotation")
   

   
    flag = 4
    iteracion = 0
    while not glfw.window_should_close(window):
        
        
        glfw.poll_events()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        valor = glfw.get_time()
        
        if(valor > flag):

                if iteracion < 4:
                    flag += 3
                elif iteracion > 4 and iteracion < 7:
                    flag += 20
                elif iteracion > 7:
                    flag += 40

           
                vertices_array, indices_array, vertices, indices = get_new_figure(vertices_array, indices_array, vertices, indices, flag, norm)
                print("\n--")
                print(iteracion+1)
                print("--\n")

                iteracion += 1
                

       

        rot_x = pyrr.Matrix44.from_x_rotation(0.5 * glfw.get_time())
        rot_x = 1
        rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time())
        
       

        glUniformMatrix4fv(rotation_loc, 1, GL_FALSE, rot_x * rot_y)

        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

        glfw.swap_buffers(window)
       
        if iteracion > 9:
            flag = 100000
       
        

    glfw.terminate()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Polyhedra Subdivision with OpenGL")

    parser.add_argument('--poly_type', dest="figure", required=False)
    parser.add_argument('--no_norm', action="store_false", required=False)

    args= parser.parse_args()

    figure = args.figure
    no_norm = args.no_norm

    if(figure == "tri" or  figure == "box" or figure == "ico" or figure == "oc"):
        pass
    else:
        figure = "oc"

    main(figure, no_norm)