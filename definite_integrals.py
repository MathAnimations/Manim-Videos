from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class DefiniteIntegrals(Scene):
    def construct(self):
        title = Tex(r"$\mathbb{D}\text{efinite}\; \mathbb{I}\text{ntegrals}$").set_color_by_gradient(PURPLE, BLUE).scale(2).move_to(UP*3.5)

        ax = Axes(
            x_range=[0, 4, 10],
            y_range=[0, 5, 20],
            x_length=6
        ).add_coordinates().scale(0.7)
        ax.move_to(UP*0.25)
        ax_labels = ax.get_axis_labels()
        ax_group = VGroup(ax, ax_labels)

        f1 = ax.plot(lambda x: x**2, x_range=[0, 2.2, 0.01], color=BLUE)
        f1_label = ax.get_graph_label(f1, label=Tex(r"$f$"), x_val=1, direction=UP + LEFT*0.5)
        f1_group = VGroup(f1, f1_label)

        a1 = ax.get_area(
            f1,
            x_range=[0.5, 2.19],
            color=[PINK, RED], opacity=0.5
        )
        a1_label = Tex(r"$A$").next_to(ax.coords_to_point(1.5, 0), UP*2.5)
        a1_group = VGroup(a1, a1_label)

        l1 = ax.get_vertical_line(ax.input_to_graph_point(0.5, f1), color=PURPLE)
        l1_label = Tex(r"$a$").next_to(ax.coords_to_point(0.5, 0), DOWN*0.3)
        l2 = ax.get_vertical_line(ax.input_to_graph_point(2.2, f1), color=PURPLE)
        l2_label = Tex(r"$b$").next_to(ax.coords_to_point(2.2, 0), DOWN*0.3)
        l1_group = VGroup(l1, l1_label, l2, l2_label)

        form1 = MathTex(r"A = \int\limits_{a}^{b}f(x)\; \text{d}x").next_to(ax, DOWN*2.25).set_color_by_gradient(PURPLE, BLUE) # form_1

        f_up = ax.plot(lambda x: 4*x - x**2, x_range=[0.268, 3.732, 0.01], color=BLUE)
        f_up_label = ax.get_graph_label(f_up, label=Tex(r"$f$"), x_val=2, direction=UP)

        f_down = ax.plot(lambda x: 0.8*x**2 - 3*x + 4, x_range=[0.268, 3.732, 0.01], color=RED)
        f_down_label = ax.get_graph_label(f_down, label=Tex(r"$g$"), x_val=2, direction=DOWN)
        f2_group = VGroup(f_up, f_up_label, f_down, f_down_label)

        a2 = ax.get_area(f_down, [0.696, 3.193], bounded_graph=f_up, color=[PINK, RED], opacity=0.5)
        a2_label = Tex(r"$A$").next_to(ax.coords_to_point(2, 1.5), UP*3)
        a2_group = VGroup(a2, a2_label)

        l3 = ax.get_vertical_line(ax.input_to_graph_point(0.696, f_down), color=PURPLE)
        l3_label = Tex(r"$a$").next_to(ax.coords_to_point(0.696, 0), DOWN*0.3)
        l4 = ax.get_vertical_line(ax.input_to_graph_point(3.193, f_down), color=PURPLE)
        l4_label = Tex(r"$b$").next_to(ax.coords_to_point(3.193, 0), DOWN*0.3)
        l2_group = VGroup(l3, l3_label, l4, l4_label)

        form2 = MathTex(r"A = \int\limits_{a}^{b}\left( f(x)-g(x)\right)\; \text{d}x").next_to(ax, DOWN*2.25).set_color_by_gradient(PURPLE, BLUE) # form_1

        form3 = MathTex(r"\int\limits_{a}^{b}f(x)\; \text{d}x &= \left[F(x)\right]_{a}^{b} \\ &= F(b)-F(a)").set_color_by_gradient(PURPLE, BLUE)

        self.play(
            Write(title),
            Create(ax_group),
            run_time=1
        )
        self.play(
            Write(f1_group)
        )
        self.play(
            Write(a1_group),
            Write(l1_group),
        )
        self.play(Write(form1))

        self.wait(2)

        self.play(
            FadeOut(a1_group),
            FadeOut(l1_group),
            Unwrite(form1),
            ReplacementTransform(f1_group, f2_group)
        )
        self.play(
            Write(a2_group),
            Write(l2_group),
            Write(form2)
        )

        self.wait(2)

        self.play(
            FadeOut(ax_group),
            FadeOut(f2_group),
            FadeOut(a2_group),
            FadeOut(l2_group),
            form2.animate.move_to(ORIGIN),
            TransformMatchingShapes(form2, form3)
        )
        self.play(Circumscribe(form3, color=RED, time_width=2))
        self.wait()
