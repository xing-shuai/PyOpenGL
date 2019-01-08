from OpenGL.GL import *
from OpenGL.GLUT import *
import PIL.Image as Image

from ctypes import c_float, c_void_p, sizeof


class Model():
    def __init__(self, vertices, indices=None, texture_path=None):
        self.vertices = vertices  # include vertex positions and texture coords
        self.indices = indices
        self.vao = glGenVertexArrays(1)
        self.init_data(texture_path)

    def init_data(self, texture_path):
        vbo = glGenBuffers(1)
        glBindVertexArray(self.vao)

        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, False, 5 * sizeof(c_float), c_void_p(0 * sizeof(c_float)))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 3, GL_FLOAT, False, 5 * sizeof(c_float), c_void_p(3 * sizeof(c_float)))
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        if texture_path:
            self.texture = self.load_texture(texture_path)
        else:
            self.texture = None

    def load_texture(self, texture_path):
        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        im = Image.open(texture_path)
        # ix, iy, image = im.size[0], im.size[1], np.array(list(im.getdata()), dtype=np.uint8)
        ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBA", 0, -1)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glGenerateMipmap(GL_TEXTURE_2D)

        return texture

    def draw(self, shader_program, texture_uniform_name="texture1", draw_type=GL_TRIANGLES):

        shader_program.use()
        if self.texture:
            glUniform1i(glGetUniformLocation(shader_program.id, texture_uniform_name), 0)
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, self.texture)

        glBindVertexArray(self.vao)

        if self.indices:
            glDrawElements(draw_type, len(self.indices), GL_UNSIGNED_INT, self.indices)

        else:
            glDrawArrays(draw_type, 0, int(len(self.vertices) / 5))

        if self.texture:
            glBindTexture(GL_TEXTURE_2D, 0)


class ModelFromExport():
    pass
