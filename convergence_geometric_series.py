from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class ConvGeometricSeries(Scene):
    config.background_color = BLACK
    def construct(self):
        q = MathTex(r"1+\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\cdots = ?")
        rec = Rectangle(color=BLUE, height=6, width=3).move_to(UP).set_fill(BLUE, opacity=0.1)

        br1 = Brace(rec, sharpness=1)
        br2 = Brace(rec, sharpness=1, direction=RIGHT)
        h = MathTex(r"2").next_to(br2, direction=RIGHT)
        w = MathTex(r"1").next_to(br1, direction=DOWN)

        frac1 = Square(side_length=3, stroke_color=RED).move_to(UP*2.5).set_fill(RED, opacity=0.1)
        frac2 = Rectangle(color=RED, height=3, width=1.5).move_to(LEFT*0.75 + DOWN*0.5).set_fill(RED, opacity=0.1)
        frac3 = Square(side_length=1.5, stroke_color=RED).move_to(RIGHT*0.75 + UP*0.25).set_fill(RED, opacity=0.1)
        frac4 = Rectangle(color=RED, height=1.5, width=0.75).move_to(RIGHT*0.37 + DOWN*1.25).set_fill(RED, opacity=0.1)
        frac5 = Square(side_length=0.75, stroke_color=RED).move_to(RIGHT*1.125 + DOWN*0.88).set_fill(RED, opacity=0.1)
        frac6 = Rectangle(color=RED, height=0.75, width=0.375).move_to(RIGHT*0.94 + DOWN*1.625).set_fill(RED, opacity=0.1)
        frac7 = Square(side_length=0.375, stroke_color=RED).move_to(RIGHT*1.313 + DOWN*1.438).set_fill(RED, opacity=0.1)
        frac8 = Rectangle(color=RED, height=0.375, width=0.1875).move_to(RIGHT*1.22 + DOWN*1.815).set_fill(RED, opacity=0.1)
        frac9 = Square(side_length=0.1875, stroke_color=RED).move_to(RIGHT*1.406 + DOWN*1.722).set_fill(RED, opacity=0.1)
        frac10 = Rectangle(color=RED, height=0.1875, width=0.09375).move_to(RIGHT*1.36 + DOWN*1.91).set_fill(RED, opacity=0.1)
        frac11 = Square(side_length=0.09375, stroke_color=RED).move_to(RIGHT*1.453 + DOWN*1.86).set_fill(RED, opacity=0.1)
        frac12 = Rectangle(color=RED, height=0.09375, width=0.046875).move_to(RIGHT*1.44 + DOWN*1.955).set_fill(RED, opacity=0.1)
        frac13 = Square(side_length=0.046875, stroke_color=RED).move_to(RIGHT*1.48 + DOWN*1.95).set_fill(RED, opacity=0.1)

        form1 = MathTex(r"1").next_to(rec, direction=DOWN*1.5)
        form2 = MathTex(r"1+\frac{1}{2}").next_to(rec, direction=DOWN*1.5)
        form3 = MathTex(r"1+\frac{1}{2}+\frac{1}{4}").next_to(rec, direction=DOWN*1.5)
        form4 = MathTex(r"1+\frac{1}{2}+\frac{1}{4}+\frac{1}{8}").next_to(rec, direction=DOWN*1.5)
        form5 = MathTex(r"1+\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}").next_to(rec, direction=DOWN*1.5)
        form6 = MathTex(r"1+\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\cdots").next_to(rec, direction=DOWN*1.5)
        form7 = MathTex(r"1+\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\cdots = 2")

        w_group = VGroup(br1, w)
        rec_group = VGroup(rec, br1, br2, h, w)


        self.play(Write(q), run_time=1)
        self.wait(2)
        self.play(ReplacementTransform(q, rec_group), run_time=0.6)

        self.wait(0.6)
        self.play(
            GrowFromCenter(frac1),
            ReplacementTransform(w_group, form1),
            FadeOut(br2, h),
            run_time=0.3
        )
        self.wait(0.6)

        self.play(
            GrowFromCenter(frac2),
            TransformMatchingShapes(form1, form2),
            run_time=0.3
        )
        self.wait(0.6)

        self.play(
            GrowFromCenter(frac3),
            TransformMatchingShapes(form2, form3),
            run_time=0.3
        )
        self.wait(0.6)

        self.play(
            GrowFromCenter(frac4),
            TransformMatchingShapes(form3, form4),
            run_time=0.3
        )
        self.wait(0.5)

        self.play(
            GrowFromCenter(frac5),
            TransformMatchingShapes(form4, form5),
            run_time=0.3
        )
        self.wait(0.6)

        self.play(LaggedStart(
            GrowFromCenter(frac6),
            GrowFromCenter(frac7),
            GrowFromCenter(frac8),
            GrowFromCenter(frac9),
            GrowFromCenter(frac10),
            GrowFromCenter(frac11),
            GrowFromCenter(frac12),
            GrowFromCenter(frac13),
            lag_ratio=0.2
            ),
            TransformMatchingShapes(form5, form6)
        )
        self.wait()

        rec_group = VGroup(rec, frac1, frac2, frac3, frac4, frac5, frac6, frac7, frac8, frac9, frac10, frac11, frac12, frac13)

        self.play(
            FadeOut(rec_group),
            form6.animate.move_to(ORIGIN)
        )
        self.play(TransformMatchingShapes(form6, form7))
        self.play(Circumscribe(form7, color=RED, time_width=2))
        self.wait()
