from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class ExponentRules(Scene):
    def construct(self):
        title = Tex(r"$\mathbb{E}\text{xponent}\; \mathbb{R}\text{ules}$").set_color_by_gradient(TEAL, BLUE).scale(2).move_to(UP*3.5)
        
        prod = MathTex(r"a^x\cdot a^y = a^{x+y}").move_to(UP*2 + LEFT*1.5).set_color_by_gradient(TEAL, BLUE)
        box_prod = SurroundingRectangle(prod, buff=0.2, color=PURPLE_B)
        prod_group = VGroup(prod, box_prod)

        quot = MathTex(r"\frac{a^x}{a^y} = a^{x-y}").next_to(prod, direction=RIGHT, buff=0.9).set_color_by_gradient(TEAL, BLUE)
        box_quot = SurroundingRectangle(quot, buff=0.2, color=PURPLE_B)
        quot_group = VGroup(quot, box_quot)

        pow = MathTex(r"\left( a^x \right)^y = a^{xy}").next_to(prod, direction=DOWN, buff=0.9).set_color_by_gradient(TEAL, BLUE)
        box_pow = SurroundingRectangle(pow, buff=0.2, color=PURPLE_B)
        pow_group = VGroup(pow, box_pow)

        pow_quot = MathTex(r"\left( \frac{a}{b} \right)^x = \frac{a^x}{b^x}").next_to(quot, direction=DOWN, buff=0.9).set_color_by_gradient(TEAL, BLUE)
        box_pow_quot = SurroundingRectangle(pow_quot, buff=0.2, color=PURPLE_B)
        pow_quot_group = VGroup(pow_quot, box_pow_quot)

        pow_prod = MathTex(r"\left( ab \right)^x = a^xb^x").next_to(pow, direction=DOWN, buff=0.9).set_color_by_gradient(TEAL, BLUE)
        box_pow_prod = SurroundingRectangle(pow_prod, buff=0.2, color=PURPLE_B)
        pow_prod_group = VGroup(pow_prod, box_pow_prod)

        zero = MathTex(r"a^0 = 1").next_to(pow_quot, direction=DOWN, buff=0.9).set_color_by_gradient(TEAL, BLUE)
        box_zero = SurroundingRectangle(zero, buff=0.2, color=PURPLE_B)
        zero_group = VGroup(zero, box_zero)

        neg_exp = MathTex(r"a^{-x} = \frac{1}{a^x}").next_to(pow_prod, direction=DOWN, buff=0.9).set_color_by_gradient(TEAL, BLUE)
        box_neg_exp = SurroundingRectangle(neg_exp, buff=0.2, color=PURPLE_B)
        neg_exp_group = VGroup(neg_exp, box_neg_exp)

        frac_exp = MathTex(r"a^{\frac{x}{y}} = \sqrt[y]{a^x}").next_to(zero, direction=DOWN, buff=0.9).set_color_by_gradient(TEAL, BLUE)
        box_frac_exp = SurroundingRectangle(frac_exp, buff=0.2, color=PURPLE_B)
        frac_exp_group = VGroup(frac_exp, box_frac_exp)
        
        self.play(Write(title))
        self.play(LaggedStart(
            GrowFromCenter(prod_group),
            GrowFromCenter(quot_group),
            GrowFromCenter(pow_group),
            GrowFromCenter(pow_quot_group),
            GrowFromCenter(pow_prod_group),
            GrowFromCenter(zero_group),
            GrowFromCenter(neg_exp_group),
            GrowFromCenter(frac_exp_group),
            lag_ratio=0.5
        ))
        self.wait(2)
