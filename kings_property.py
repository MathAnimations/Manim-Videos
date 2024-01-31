from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class KingsProperty(Scene):
    def construct(self):   
        title = Text("King´s Property").scale(0.9).shift(UP*3).set_color(RED)
        f1 = MathTex(r"\int\limits_{a}^{b}f(x)\; \text{d}x = \int\limits_{a}^{b}f(a+b-x)\; \text{d}x").set_color(RED)
        f2 = MathTex(r"I=\int\limits_{0}^{\frac{\pi}{2}}\ln (\sin (x))\; \text{d}x")
        f3 = MathTex(r"I=\int\limits_{0}^{\frac{\pi}{2}}\ln \left(\sin \left( \frac{\pi}{2}-x\right) \right)\; \text{d}x")
        f4 = MathTex(r"I=\int\limits_{0}^{\frac{\pi}{2}}\ln (\cos (x))\; \text{d}x")
        f5 = MathTex(r"2I=\int\limits_{0}^{\frac{\pi}{2}}\ln (\sin (x)) + \ln (\cos (x)) \; \text{d}x")
        f6 = MathTex(r"2I=\int\limits_{0}^{\frac{\pi}{2}}\ln \left( \frac{1}{2}\sin (2x) \right) \; \text{d}x")
        f7 = MathTex(r"2I = \int\limits_{0}^{\frac{\pi}{2}}\ln (\sin (2x))-\ln (2)\; \text{d}x")
        f8 = MathTex(r"2I = \frac{1}{2}\int\limits_{0}^{\pi}\ln (\sin (x))\; \text{d}x - \frac{1}{2}\int\limits_{0}^{\pi}\ln (2)\; \text{d}x")
        f9 = MathTex(r"2I = \int\limits_{0}^{\frac{\pi}{2}}\ln (\sin (x))\; \text{d}x - \frac{1}{2}\int\limits_{0}^{\pi}\ln (2)\; \text{d}x")
        f10 = MathTex(r"2I = I - \frac{1}{2}\int\limits_{0}^{\pi}\ln (2)\; \text{d}x")
        f11 = MathTex(r"I = - \frac{1}{2}\int\limits_{0}^{\pi}\ln (2)\; \text{d}x")
        f12 = MathTex(r"I = -\frac{\pi}{2}\ln (2)")

        self.play(
            Write(title),
            Write(f1),
            run_time=1
        )

        self.play(
            Circumscribe(f1, color=RED, time_width=1)
        )

        group = VGroup(title, f1)
        self.wait(0.5)
        rt = 0.5
        self.play(
            TransformMatchingShapes(group, f2),
            run_time=rt
        )

        self.play(
            TransformMatchingShapes(f2, f3),
            run_time=rt
        )

        self.play(
            TransformMatchingShapes(f3, f4),
            run_time=rt
        )

        self.wait(1.3)
      
        self.play(
            TransformMatchingShapes(f4, f5),
            run_time=rt
        )

        self.play(
            TransformMatchingShapes(f5, f6),
            run_time=rt
        )

        self.play(
            TransformMatchingShapes(f6, f7),
            run_time=rt
        )

        self.wait(1.2)

        self.play(
            TransformMatchingShapes(f7, f8),
            run_time=rt
        )

        self.play(
            TransformMatchingShapes(f8, f9),
            run_time=rt
        )

        self.play(
            TransformMatchingShapes(f9, f10),
            run_time=rt
        )

        self.wait(1.2)

        self.play(
            TransformMatchingShapes(f10, f11),
            run_time=rt
        )

        self.play(
            TransformMatchingShapes(f11, f12),
            run_time=rt
        )

        self.play(
            Circumscribe(f12, color=RED, time_width=2)
        )
