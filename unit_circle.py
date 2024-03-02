from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class UnitCirc(Scene):
    def construct(self):
        title = Tex(r"$\mathbb{U}\text{nit}\; \mathbb{C}\text{ircle}$").set_color_by_gradient(RED, PURPLE).scale(2).move_to(UP*3.5)

        ax = Axes(
            x_range=[-1.3, 1.3],
            y_range=[-1.3, 1.3],
            x_length=6,
            tips=False
        ).add_coordinates().scale(0.865)

        circ = Circle(radius=2, color=RED).set_stroke(opacity=0.5)
        

        h = Line(start=[0, 0, 0], end=[0.7071*2, 0.7071*2, 0], color=PURPLE)
        k1 = Line(start=[0, 0, 0], end=[0.7071*2, 0, 0], color=PURPLE)
        k2 = Line(start=k1.get_end(), end=h.get_end(), color=PURPLE)
        triangle = VGroup(h, k1, k2)

        angle = Angle(
            line1=k1,
            line2=h,
            color=RED
        )

        h_label = Tex(r"1").set_color(PURPLE_B).scale(0.8).next_to(h.get_center(), direction=LEFT).shift(UP*0.2 + RIGHT*0.1)
        k1_label = Tex(r"$\cos \alpha$").set_color(PURPLE_B).scale(0.8).next_to(k1.get_center(), direction=DOWN).shift(UP*0.1)
        k2_label = Tex(r"$\sin \alpha$").set_color(PURPLE_B).scale(0.8).next_to(k2.get_center(), direction=RIGHT).shift(LEFT*0.1)
        angle_label = Tex(r"$\alpha$").set_color(RED).scale(0.8).next_to(angle.get_center(), RIGHT).shift(UP*0.1)
        labels = VGroup(h_label, k1_label, k2_label, angle_label)

        self.play(Write(title))
        self.play(
            Create(ax),
            Create(circ)
        )
        self.play(
            Create(triangle),
            Create(angle)
        )
        self.play(Write(labels))
        
        form = MathTex(r"\sin^2 \alpha + \cos^2 \alpha = 1").scale(0.9).next_to(ax, direction=DOWN).set_color_by_gradient(RED, PURPLE)

        self.play(GrowFromCenter(form))
        self.wait(2.5)
