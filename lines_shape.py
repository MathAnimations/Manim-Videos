from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class LinesShape(Scene):
    def construct(self):
        c1 = Dot(color=RED)
        c2 = c1.copy()
        c3 = c1.copy()
        c4 = c1.copy()
        c5 = c1.copy()
        c6 = c1.copy()
        c7 = c1.copy()
        c8 = c1.copy()
        dots = VGroup(c1, c2, c3, c4, c5, c6, c7, c8)
        paths = VGroup(*[
            TracedPath(lambda c=c: c.get_center(), stroke_width=3, stroke_color=RED)
            for c in dots
        ])
        directions = (RIGHT, LEFT, UP, DOWN, DL, DR, UL, UR)

        self.play(GrowFromCenter(c1))
        self.add(dots, paths)
        self.play(
            *[
                c.animate(path_arc=PI).shift(direction*3)
                for c, direction in zip(dots, directions)
            ],
            rate_func=linear, run_time=2
        )
        self.play(
            *[c.animate(path_arc=PI).move_to(ORIGIN) for c in dots],
            rate_func=linear, run_time=2
        )

        intersections = VGroup(*[
            Intersection(path1, path2, color=PURPLE_C, stroke_width=4).set_fill(color=TEAL, opacity=0.5)
            for path1, path2 in it.permutations(paths, 2)
        ])

        self.play(*[FadeIn(x) for x in intersections], rate_func=linear)
        self.wait()
