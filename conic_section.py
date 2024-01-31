from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class ConicSectionCircle(ThreeDScene):
    def construct(self):
        r = 2
        cone = Cone(r, r).set_fill(TEAL, 0.2)
        cone.next_to(ORIGIN, OUT, buff=0)
        plane = Square(2 * r + 1).set_fill(PURPLE, 0.1)
        circle = Circle(r).set_stroke(RED, 3)
 
        def upd_circle(circ):
            height = plane.get_center()[2]
            circ.move_to(height * OUT)
            new_radius = r - height
            circ.set(width=2*new_radius)
 
        circle.add_updater(upd_circle)

        self.play(
            Create(plane)
        )
        self.move_camera(phi=75*DEGREES, theta=45*DEGREES)

        self.play(
            Create(cone),
            Write(circle)
        )
        self.play(plane.animate.shift(2*OUT), run_time=4)
        self.wait()
        self.play(
            Uncreate(cone),
            Unwrite(circle),
            Uncreate(plane)
        )
