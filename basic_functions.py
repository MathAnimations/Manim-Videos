from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class BasicFunctions(Scene):
    def construct(self):
        title = Tex(r"$\mathbb{B}\text{asic}\; \mathbb{F}\text{unctions}$").set_color_by_gradient(GREEN, TEAL).scale(2).move_to(UP*3)

        ax = Axes(
            x_range=[-4, 4, 10],
            y_range=[-10, 10, 20],
            x_length=6
        ).add_coordinates()
        ax.move_to(DOWN)
        ax_labels = ax.get_axis_labels()
        ax_group = VGroup(ax, ax_labels)

        f1 = ax.plot(lambda x: 5, x_range=[-4, 4, 0.01], color=GREEN)
        f1_label = ax.get_graph_label(f1, label=Tex(r"$\text{const}$"), x_val=2, direction=UP*1)
        f1_group = VGroup(f1, f1_label)

        f2 = ax.plot(lambda x: x, x_range=[-4, 4, 0.01], color=GREEN)
        f2_label = ax.get_graph_label(f2, label=Tex(r"$x$"), x_val=2, direction=UP*1.5)
        f2_group = VGroup(f2, f2_label)

        f3 = ax.plot(lambda x: x**2, x_range=[-3, 3, 0.01], color=GREEN)
        f3_label = ax.get_graph_label(f3, label=Tex(r"$x^2$"), x_val=2, direction=UP*1.5 + LEFT*0.1)
        f3_group = VGroup(f3, f3_label)

        f4 = ax.plot(lambda x: x**3, x_range=[-2, 2, 0.01], color=GREEN)
        f4_label = ax.get_graph_label(f4, label=Tex(r"$x^3$"), x_val=2, direction=LEFT*1)
        f4_group = VGroup(f4, f4_label)

        f5 = ax.plot(lambda x: x**(1/2), x_range=[0, 4, 0.01], color=GREEN)
        f5_label = ax.get_graph_label(f5, label=Tex(r"$\sqrt{x}$"), x_val=2, direction=UP*1)
        f5_group = VGroup(f5, f5_label)

        f6 = ax.plot(lambda x: 1/x, x_range=[-4, -0.1, 0.01], color=GREEN)
        f6_2 = ax.plot(lambda x: 1/x, x_range=[0.1, 4, 0.01], color=GREEN)
        f6_label = ax.get_graph_label(f6_2, label=Tex(r"$\frac{1}{x}$"), x_val=2, direction=UP*1)
        f6_group = VGroup(f6, f6_label, f6_2)

        f7 = ax.plot(lambda x: 1/(x**2), x_range=[-4, -0.316, 0.01], color=GREEN)
        f7_2 = ax.plot(lambda x: 1/(x**2), x_range=[0.316, 4, 0.01], color=GREEN)
        f7_label = ax.get_graph_label(f7_2, label=Tex(r"$\frac{1}{x^2}$"), x_val=2, direction=UP*1)
        f7_group = VGroup(f7, f7_label, f7_2)

        f8 = ax.plot(lambda x: np.log(x), x_range=[0.00005, 4, 0.01], color=GREEN)
        f8_label = ax.get_graph_label(f8, label=Tex(r"$\ln x$"), x_val=2, direction=UP*1)
        f8_group = VGroup(f8, f8_label)

        f9 = ax.plot(lambda x: np.exp(x), x_range=[-4, 2.3, 0.01], color=GREEN)
        f9_label = ax.get_graph_label(f9, label=Tex(r"$e^x$"), x_val=2, direction=DOWN*2)
        f9_group = VGroup(f9, f9_label)

        f10 = ax.plot(lambda x: np.sin(x), x_range=[-4, 4, 0.01], color=GREEN)
        f10_label = ax.get_graph_label(f10, label=Tex(r"$\sin x$"), x_val=2, direction=UP*1)
        f10_group = VGroup(f10, f10_label)

        f11 = ax.plot(lambda x: np.cos(x), x_range=[-4, 4, 0.01], color=GREEN)
        f11_label = ax.get_graph_label(f11, label=Tex(r"$\cos x$"), x_val=2, direction=UP*1.5)
        f11_group = VGroup(f11, f11_label)

        wt = 1
        rt = 0.25

        self.play(
            Write(title),
            Create(ax_group),
            run_time=1
        )

        self.play(Write(f1_group), run_time=1.2)
        self.wait(wt)

        self.play(
            ReplacementTransform(f1_group, f2_group),
            run_time=rt
        )
        self.wait(wt)

        self.play(
            ReplacementTransform(f2_group, f3_group),
            run_time=rt
        )
        self.wait(wt)

        self.play(
            ReplacementTransform(f3_group, f4_group),
            run_time=rt
        )
        self.wait(wt)

        self.play(
            ReplacementTransform(f4_group, f5_group),
            run_time=rt
        )
        self.wait(wt)

        self.play(
            ReplacementTransform(f5_group, f6_group),
            run_time=rt
        )
        self.wait(wt)

        self.play(
            ReplacementTransform(f6_group, f7_group),
            run_time=rt
        )
        self.wait(wt)

        self.play(
            ReplacementTransform(f7_group, f8_group),
            run_time=rt
        )
        self.wait(wt)

        self.play(
            ReplacementTransform(f8_group, f9_group),
            run_time=rt
        )
        self.wait(wt)

        self.play(
            ReplacementTransform(f9_group, f10_group),
            run_time=rt
        )
        self.wait(wt)

        self.play(
            ReplacementTransform(f10_group, f11_group),
            run_time=rt
        )
        self.wait(wt)
