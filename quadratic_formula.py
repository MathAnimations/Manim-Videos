from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class QuadraticFormula(Scene):
    def construct(self):
        f1 = MathTex(r"ax^2+bx+c = 0")
        f2 = MathTex(r"x^2 + \frac{b}{a}x + \frac{c}{a} = 0")
        f3 = MathTex(r"x^2 + \frac{b}{a}x + \left( \frac{b}{2a} \right)^2 - \left( \frac{b}{2a} \right)^2 + \frac{c}{a} = 0").scale(0.8)
        f4 = MathTex(r"\left( x + \frac{b}{2a} \right)^2 - \left( \frac{b}{2a} \right)^2 + \frac{c}{a} = 0")
        f5 = MathTex(r"\left( x + \frac{b}{2a} \right)^2 = \left( \frac{b}{2a} \right)^2 - \frac{c}{a}")
        f6 = MathTex(r"x_{1/2} + \frac{b}{2a} = \pm \sqrt{\left( \frac{b}{2a} \right)^2 - \frac{c}{a}}")
        f7 = MathTex(r"x_{1/2} + \frac{b}{2a} = \pm \sqrt{\frac{b^2 - 4ac}{4a^2}}")
        f8 = MathTex(r"x_{1/2} = - \frac{b}{2a}\pm \sqrt{\frac{b^2 - 4ac}{4a^2}}")
        f9 = MathTex(r"x_{1/2} = - \frac{b}{2a}\pm \frac{\sqrt{b^2-4ac}}{2a}")
        f10 = MathTex(r"x_{1/2} = \frac{-b\pm \sqrt{b^2-4ac}}{2a}")

        rt = 0.7
        self.play(Write(f1))
        self.play(TransformMatchingShapes(f1, f2), run_time=0.5)
        self.play(TransformMatchingShapes(f2, f3), run_time=rt)
        self.play(TransformMatchingShapes(f3, f4), run_time=rt)
        self.play(TransformMatchingShapes(f4, f5), run_time=rt)
        self.play(TransformMatchingShapes(f5, f6), run_time=rt)
        self.play(TransformMatchingShapes(f6, f7), run_time=rt)
        self.play(TransformMatchingShapes(f7, f8), run_time=rt)
        self.play(TransformMatchingShapes(f8, f9), run_time=rt)
        self.play(TransformMatchingShapes(f9, f10), run_time=rt)
        self.play(Circumscribe(f10, shape=Rectangle, color=RED), run_time=rt*2)
        self.wait(rt*3)
