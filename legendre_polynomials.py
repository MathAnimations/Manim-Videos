from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class LegendrePol(Scene):
    def construct(self):
        title = Tex(r"$\mathbb{L}\text{egendre}\; \mathbb{P}\text{olynomials}$").set_color_by_gradient(PURPLE, RED).scale(1.5).move_to(UP*3.5)
        
        ax = Axes(
            x_range=[-1, 1, 0.5],
            y_range=[-1, 1, 0.5],
            x_length=6,
            tips=False,
        ).add_coordinates().scale(0.75)
        ax.move_to(UP*0.2)
        ax_labels = ax.get_axis_labels()
        ax_group = VGroup(ax, ax_labels)

        form = MathTex(r"P_n(x) = \sum_{k=0}^{\lfloor \frac{n}{2}\rfloor}(-1)^k \frac{(2n-2k)!}{2^nk!(n-k)!(n-2k)!}x^{n-2k}").scale(0.7)

        p0 = ax.plot(lambda x: 1, x_range=[-1, 1, 0.01], color=PURPLE_B)
        p1 = ax.plot(lambda x: x, x_range=[-1, 1, 0.01], color=PURPLE_C)
        p2 = ax.plot(lambda x: 0.5*(3*x**2 -1), x_range=[-1, 1, 0.01], color=PURPLE_D)
        p3 = ax.plot(lambda x: 0.5*(5*x**3 -3*x), x_range=[-1, 1, 0.01], color=MAROON_C)
        p4 = ax.plot(lambda x: (1/8)*(35*x**4 -30*x**2 +3), x_range=[-1, 1, 0.01], color=RED_C)
        p5 = ax.plot(lambda x: (1/8)*(63*x**5 -70*x**3 +15*x), x_range=[-1, 1, 0.01], color=RED_E)
        p6 = ax.plot(lambda x: (1/16)*(231*x**6 -315*x**4 +105*x**2 -5), x_range=[-1, 1, 0.01], color=RED)

        p0_t = MathTex(r"P_0(x)=1").set_color_by_gradient(PURPLE, RED).next_to(ax, DOWN*1.5).scale(0.8)
        p1_t = MathTex(r"P_1(x)=x").set_color_by_gradient(PURPLE, RED).next_to(ax, DOWN*1.5).scale(0.8)
        p2_t = MathTex(r"P_2(x)=\frac{1}{2}\left( 3x^2 - 1 \right)").set_color_by_gradient(PURPLE, RED).next_to(ax, DOWN*1.5).scale(0.8)
        p3_t = MathTex(r"P_3(x)=\frac{1}{2}\left( 5x^3 - 3x \right)").set_color_by_gradient(PURPLE, RED).next_to(ax, DOWN*1.5).scale(0.8)
        p4_t = MathTex(r"P_4(x)=\frac{1}{8}\left( 35x^4 - 30x^2 + 3 \right)").set_color_by_gradient(PURPLE, RED).next_to(ax, DOWN*1.5).scale(0.8)
        p5_t = MathTex(r"P_5(x)=\frac{1}{8}\left( 63x^5 - 70x^3 + 15x \right)").set_color_by_gradient(PURPLE, RED).next_to(ax, DOWN*1.5).scale(0.8)
        p6_t = MathTex(r"P_6(x)=\frac{1}{16}\left( 231x^6 - 315x^4 + 105x^2 -5 \right)").set_color_by_gradient(PURPLE, RED).next_to(ax, DOWN*1.5).scale(0.8)

        self.play(
            Write(title),
            Write(form)
        )
        self.play(
            Circumscribe(form, time_width=2, color=RED),
            form.animate.set_color_by_gradient(PURPLE, RED)
        )
        self.wait()
        self.play(ReplacementTransform(form, ax_group))
        self.play(
            Write(p0_t),
            Write(p0)
        )
        self.wait(0.5)
        self.play(
            Write(p1),
            TransformMatchingShapes(p0_t, p1_t)
        )
        self.wait(0.5)
        self.play(
            Write(p2),
            TransformMatchingShapes(p1_t, p2_t)
        )
        self.wait(0.5)
        self.play(
            Write(p3),
            TransformMatchingShapes(p2_t, p3_t)
        )
        self.wait(0.5)
        self.play(
            Write(p4),
            TransformMatchingShapes(p3_t, p4_t)
        )
        self.wait(0.5)
        self.play(
            Write(p5),
            TransformMatchingShapes(p4_t, p5_t)
        )
        self.wait(0.5)
        self.play(
            Write(p6),
            TransformMatchingShapes(p5_t, p6_t)
        )
        self.wait(2)
