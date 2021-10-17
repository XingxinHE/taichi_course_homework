import taichi as ti

ti.init(arch=ti.gpu)

N = 500
UNIVERSUS = ti.field(dtype=float, shape=(N * 2, N))

@ti.kernel
def create():
    for i, j in UNIVERSUS:
        UNIVERSUS[i, j] = 0

gui = ti.GUI("Universus", res=(N * 2, N))

while gui.running:
    create()
    gui.set_image(UNIVERSUS)
    gui.show()