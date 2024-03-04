from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class ChebPol(Scene):
    def construct(self):
        title = Tex(r"$\mathbb{C}\text{hebyshev}\; \mathbb{P}\text{olynomials}$").set_color_by_gradient(TEAL, GREEN).scale(1.5).move_to(UP*3.5)

        form = MathTex(r"T_0 (x) &= 1 \\ T_1(x) &= x \\ T_{n+1}(x) &= 2xT_n(x) - T_{n-1}(x)")

        ax = Axes(
            x_range=[-1, 1, 0.5],
            y_range=[-1.1, 1, 0.5],
            x_length=7,
            tips=False
        ).add_coordinates().scale(0.75)
        ax.move_to(UP*0.2)
        ax_labels = ax.get_axis_labels()

        ax_group = VGroup(ax, ax_labels)

        t0 = ax.plot(lambda x: 1, x_range=[-1, 1, 0.01], color=TEAL_A)
        t1 = ax.plot(lambda x: x, x_range=[-1, 1, 0.01], color=TEAL_C)
        t2 = ax.plot(lambda x: 2*x**2 - 1, x_range=[-1, 1, 0.01], color=TEAL_E)
        t3 = ax.plot(lambda x: 4*x**3 - 3*x, x_range=[-1, 1, 0.01], color=GREEN_A)
        t4 = ax.plot(lambda x: 8*x**4 - 8*x**2 + 1, x_range=[-1, 1, 0.01], color=GREEN_C)
        t5 = ax.plot(lambda x: 16*x**5 - 20*x**3 + 5*x, x_range=[-1, 1, 0.01], color=GREEN_E)

        form_t0 = MathTex(r"T_0 (x)=1").set_color_by_gradient(TEAL, GREEN).next_to(ax, DOWN*1.5).scale(0.9)
        form_t1 = MathTex(r"T_1 (x)=x").set_color_by_gradient(TEAL, GREEN).next_to(ax, DOWN*1.5).scale(0.9)
        form_t2 = MathTex(r"T_2 (x)=2x^2-1").set_color_by_gradient(TEAL, GREEN).next_to(ax, DOWN*1.5).scale(0.9)
        form_t3 = MathTex(r"T_3 (x)=4x^3-3x").set_color_by_gradient(TEAL, GREEN).next_to(ax, DOWN*1.5).scale(0.9)
        form_t4 = MathTex(r"T_4 (x)=8x^4-8x^2+1").set_color_by_gradient(TEAL, GREEN).next_to(ax, DOWN*1.5).scale(0.9)
        form_t5 = MathTex(r"T_5 (x)=16x^5-20x^3+5x").set_color_by_gradient(TEAL, GREEN).next_to(ax, DOWN*1.5).scale(0.9)

        self.play(
            Write(title),
            Write(form)
        )
        self.play(
            Circumscribe(form, time_width=2, color=GREEN),
            form.animate.set_color_by_gradient(TEAL, GREEN)
        )
        self.wait()
        self.play(ReplacementTransform(form, ax_group))
        self.play(
            Write(t0),
            Write(form_t0)
        )
        self.wait(1)
        self.play(
            Write(t1),
            TransformMatchingShapes(form_t0, form_t1)
        )
        self.wait(1)
        self.play(
            Write(t2),
            TransformMatchingShapes(form_t1, form_t2)
        )
        self.wait(1)
        self.play(
            Write(t3),
            TransformMatchingShapes(form_t2, form_t3)
        )
        self.wait(1)
        self.play(
            Write(t4),
            TransformMatchingShapes(form_t3, form_t4)
        )
        self.wait(1)
        self.play(
            Write(t5),
            TransformMatchingShapes(form_t4, form_t5)
        )
        self.wait(1)
