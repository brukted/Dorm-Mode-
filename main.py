import sys

import pygame as pg
from OpenGL.GL import *

from constants import DEFAULT_WINDOW_SIZE, FPS_LIMIT, WINDOW_TITLE
from core.context import Context


def load_assets(context: Context):
    """Loads the dorm model, textures and shaders."""
    context.load_texture('grid', 'assets/grid.png')
    context.load_texture('chair_one_tex', 'assets/CHAIR_ONE_TEX.png')
    context.load_texture('chair_2_tex', 'assets/CHAIR_2_TEX.png')
    context.load_texture('wall_tex', 'assets/WALL_TEX.png')
    context.load_texture('celling_tex', 'assets/CELLING_TEX.png')
    context.load_texture('books_tex', 'assets/BOOKS_TEX.png')
    context.load_texture('cabinate_1_tex', 'assets/CABINATE_1_TEX.png')
    context.load_texture('cabinate_2_tex', 'assets/CABINATE_2_TEX.png')
    context.load_texture('matress_1_tex', 'assets/MATRESS_1_TEX.png')
    context.load_texture('matress_2_tex', 'assets/MATRESS_2_TEX.png')
    context.load_texture('matress_3_tex', 'assets/MATRESS_3_TEX.png')
    context.load_texture('matress_4_tex', 'assets/MATRESS_4_TEX.png')
    context.load_texture('floor_tex', 'assets/FLOOR_TEX.png')
    context.load_texture('table_tex', 'assets/TABLE_TEX.png')
    context.load_texture('papers_1_tex', 'assets/PAPERS_1_TEX.png')
    context.load_texture('papers_2_tex', 'assets/PAPERS_2_TEX.png')
    context.load_texture('bed_1_tex', 'assets/BED_1_TEX.png')
    context.load_texture('bed_2_tex', 'assets/BED_2_TEX.png')
    context.load_texture('bed_3_tex', 'assets/BED_3_TEX.png')
    context.load_texture('bed_4_tex', 'assets/BED_4_TEX.png')
    context.load_texture('lamp_tex', 'assets/LAMP_TEX.png')
    context.load_texture('mug_tex', 'assets/MUG_TEX.png')
    context.load_texture('wood_plane_1_tex', 'assets/WOOD_PLANE_1_TEX.png')
    context.load_texture('wood_plane_2_tex', 'assets/WOOD_PLANE_2_TEX.png')

    default_shader = context.load_shader(
        'default_shader', 'assets/vertex_shader.vert', 'assets/fragment_shader.frag')

    context.create_material("books", "default_shader", {
        'texture': ("texture", 'books_tex', 0)
    })

    context.create_material("papers_2", "default_shader", {
        'texture': ("texture", 'papers_2_tex', 0)
    })

    context.create_material("cabinate_1", "default_shader", {
        'texture': ("texture", 'cabinate_1_tex', 0)
    })

    context.create_material("cabinate_2", "default_shader", {
        'texture': ("texture", 'cabinate_2_tex', 0)
    })

    context.create_material("matress_1", "default_shader", {
        'texture': ("texture", 'matress_1_tex', 0)
    })

    context.create_material("matress_2", "default_shader", {
        'texture': ("texture", 'matress_2_tex', 0)
    })

    context.create_material("matress_3", "default_shader", {
        'texture': ("texture", 'matress_3_tex', 0)
    })

    context.create_material("matress_4", "default_shader", {
        'texture': ("texture", 'matress_4_tex', 0)
    })

    context.create_material("default_material", "default_shader", {
        'texture': ("texture", 'grid', 0)
    })

    context.create_material("chair_one", "default_shader", {
        'texture': ("texture", 'chair_one_tex', 0)
    })

    context.create_material("chair_two", "default_shader", {
        'texture': ("texture", 'chair_2_tex', 0)
    })

    context.create_material("wall", "default_shader", {
        'texture': ("texture", 'wall_tex', 0)
    })

    context.create_material("celling", "default_shader", {
        'texture': ("texture", 'celling_tex', 0)
    })

    context.create_material("floor", "default_shader", {
        'texture': ("texture", 'floor_tex', 0)
    })

    context.create_material("table", "default_shader", {
        'texture': ("texture", 'table_tex', 0)
    })

    context.create_material("papers_1", "default_shader", {
        'texture': ("texture", 'papers_1_tex', 0)
    })

    context.create_material("bed_1", "default_shader", {
        'texture': ("texture", 'bed_1_tex', 0)
    })

    context.create_material("bed_2", "default_shader", {
        'texture': ("texture", 'bed_2_tex', 0)
    })

    context.create_material("bed_3", "default_shader", {
        'texture': ("texture", 'bed_3_tex', 0)
    })

    context.create_material("bed_4", "default_shader", {
        'texture': ("texture", 'bed_4_tex', 0)
    })

    context.create_material("lamp", "default_shader", {
        'texture': ("texture", 'lamp_tex', 0)
    })

    context.create_material("mug", "default_shader", {
        'texture': ("texture", 'mug_tex', 0)
    })

    context.create_material("wood_plane_1", "default_shader", {
        'texture': ("texture", 'wood_plane_1_tex', 0)
    })

    context.create_material("wood_plane_2", "default_shader", {
        'texture': ("texture", 'wood_plane_2_tex', 0)
    })

    chair_one = context.scene.load_mesh('assets/CHAIR_ONE.obj')
    chair_one.material_name = 'chair_one'

    chair_two = context.scene.load_mesh('assets/CHAIR_2.obj')
    chair_two.material_name = 'chair_two'

    wall = context.scene.load_mesh('assets/WALL.obj')
    wall.material_name = 'wall'

    ceiling = context.scene.load_mesh('assets/CELLING.obj')
    ceiling.material_name = 'celling'

    floor = context.scene.load_mesh('assets/FLOOR.obj')
    floor.material_name = 'floor'

    table = context.scene.load_mesh('assets/TABLE.obj')
    table.material_name = 'table'

    papers_1 = context.scene.load_mesh('assets/PAPERS_1.obj')
    papers_1.material_name = 'papers_1'

    books = context.scene.load_mesh('assets/BOOKS.obj')
    books.material_name = 'books'

    cabinate_1 = context.scene.load_mesh('assets/CABINATE_1.obj')
    cabinate_1.material_name = 'cabinate_1'

    cabinate_2 = context.scene.load_mesh('assets/CABINATE_2.obj')
    cabinate_2.material_name = 'cabinate_2'

    matress_1 = context.scene.load_mesh('assets/MATRESS_1.obj')
    matress_1.material_name = 'matress_1'

    matress_2 = context.scene.load_mesh('assets/MATRESS_2.obj')
    matress_2.material_name = 'matress_2'

    matress_3 = context.scene.load_mesh('assets/MATRESS_3.obj')
    matress_3.material_name = 'matress_3'

    matress_4 = context.scene.load_mesh('assets/MATRESS_4.obj')
    matress_4.material_name = 'matress_4'

    matress_8 = context.scene.load_mesh('assets/MATRESS_8.obj')
    matress_8.material_name = 'matress_8'

    matress_5 = context.scene.load_mesh('assets/MATRESS_5.obj')
    matress_5.material_name = 'matress_5'

    papers_2 = context.scene.load_mesh('assets/PAPERS_2.obj')
    papers_2.material_name = 'papers_2'

    bed_1 = context.scene.load_mesh('assets/BED_1.obj')
    bed_1.material_name = 'bed_1'

    bed_2 = context.scene.load_mesh('assets/BED_2.obj')
    bed_2.material_name = 'bed_2'

    bed_3 = context.scene.load_mesh('assets/BED_3.obj')
    bed_3.material_name = 'bed_3'

    bed_4 = context.scene.load_mesh('assets/BED_4.obj')
    bed_4.material_name = 'bed_4'

    lamp = context.scene.load_mesh('assets/LAMP.obj')
    lamp.material_name = 'lamp'

    mug = context.scene.load_mesh('assets/MUG.obj')
    mug.material_name = 'mug'

    wood_plane_1 = context.scene.load_mesh('assets/WOOD_PLANE_1.obj')
    wood_plane_1.material_name = 'wood_plane_1'

    wood_plane_2 = context.scene.load_mesh('assets/WOOD_PLANE_2.obj')
    wood_plane_2.material_name = 'wood_plane_2'

    # Compile Shaders
    default_shader.compile()


def main():
    """Main function."""
    context = Context()

    # Window creation and OpenGL context creation
    init_pygame()

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    # Loads the dorm model, textures and shaders
    load_assets(context)

    glClearColor(0., 0., 0., 1)
    glEnable(GL_MULTISAMPLE)

    dt = 0
    clock = pg.time.Clock()
    clock.tick(FPS_LIMIT)

    # Main event loop
    forward_motion = 0.0
    right_motion = 0.0
    up_motion = 0.0

    while True:
        # Input processing

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.VIDEORESIZE:
                context.camera.aspect_ratio = event.w / event.h
                context.camera.window_size = event.w, event.h
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    forward_motion = 1.0
                elif event.key == pg.K_s:
                    forward_motion = -1.0
                elif event.key == pg.K_a:
                    right_motion = -1.0
                elif event.key == pg.K_d:
                    right_motion = 1.0
                elif event.key == pg.K_e:
                    up_motion = 1.0
                elif event.key == pg.K_q:
                    up_motion = -1.0

            elif event.type == pg.KEYUP:
                if event.key == pg.K_w or event.key == pg.K_s:
                    forward_motion = 0.0
                if event.key == pg.K_a or event.key == pg.K_d:
                    right_motion = 0.0
                if event.key == pg.K_e or event.key == pg.K_q:
                    up_motion = 0.0

        if pg.mouse.get_pressed()[0]:
            delta_mouse = pg.mouse.get_rel()
            context.camera.update(
                delta_mouse, forward_motion, right_motion, up_motion, dt)
        else:
            pg.mouse.get_rel()
            context.camera.update((0, 0), forward_motion,
                                  right_motion, up_motion, dt)

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        context.scene.draw(context)

        # Swap front and back buffers
        pg.display.flip()

        dt = clock.tick(FPS_LIMIT) / 1000.0


def init_pygame():
    pg.init()

    pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 4)
    pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 1)
    pg.display.gl_set_attribute(
        pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

    pg.display.set_mode(DEFAULT_WINDOW_SIZE,
                        pg.DOUBLEBUF | pg.OPENGL | pg.RESIZABLE)
    pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
    pg.display.set_caption(WINDOW_TITLE)


if __name__ == "__main__":
    main()
