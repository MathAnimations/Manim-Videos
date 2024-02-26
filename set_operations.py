from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class SetOperations(Scene):
    def construct(self):
        title = Tex(r"$\mathbb{S}\text{et}\; \mathbb{O}\text{perations}$").set_color_by_gradient(RED, GOLD).scale(2).move_to(UP*3.5)

        set1 = Circle(radius=2, color=RED).move_to(LEFT)
        set1_label = MathTex(r"A").set_color(RED).next_to(set1, direction=DOWN)
        set1_group = VGroup(set1, set1_label)

        set2 = Circle(radius=2, color=GOLD).move_to(RIGHT)
        set2_label = MathTex(r"B").set_color(GOLD).next_to(set2, direction=DOWN)
        set2_group = VGroup(set2, set2_label)

        intersection = Intersection(set1, set2, color=ORANGE, fill_opacity=0.5)
        union = Union(set1, set2, color=ORANGE, fill_opacity=0.5)
        diff1 = Difference(set1, set2, color=ORANGE, fill_opacity=0.5)
        diff2 = Difference(set2, set1, color=ORANGE, fill_opacity=0.5)
        exclusion = Exclusion(set1, set2, color=ORANGE, fill_opacity=0.5)

        form_intersection = MathTex(r"A\cap B").move_to(DOWN*3.5).set_color_by_gradient(RED, GOLD)
        box_intersection = SurroundingRectangle(form_intersection, buff=0.2, color=RED)
        form_intersection_group = VGroup(form_intersection, box_intersection)

        form_union = MathTex(r"A\cup B").move_to(DOWN*3.5).set_color_by_gradient(RED, GOLD)
        box_union = SurroundingRectangle(form_union, buff=0.2, color=RED)
        form_union_group = VGroup(form_union, box_union)
        
        form_diff1 = MathTex(r"A\setminus B").move_to(DOWN*3.5).set_color_by_gradient(RED, GOLD)
        box_diff1 = SurroundingRectangle(form_diff1, buff=0.2, color=RED)
        form_diff1_group = VGroup(form_diff1, box_diff1)

        form_diff2 = MathTex(r"B\setminus A").move_to(DOWN*3.5).set_color_by_gradient(GOLD, RED)
        box_diff2 = SurroundingRectangle(form_diff2, buff=0.2, color=RED)
        form_diff2_group = VGroup(form_diff2, box_diff2)

        form_exclusion = MathTex(r"A\bigtriangleup B").move_to(DOWN*3.5).set_color_by_gradient(RED, GOLD)
        box_exclusion = SurroundingRectangle(form_exclusion, buff=0.2, color=RED)
        form_exclusion_group = VGroup(form_exclusion, box_exclusion)

        self.play(
            Write(title),
            Create(set1_group),
            Create(set2_group)
        )

        self.play(
            GrowFromCenter(intersection),
            Write(form_intersection_group)
        )
        self.wait(2)

        self.play(
            ReplacementTransform(intersection, union),
            TransformMatchingShapes(form_intersection_group, form_union_group)
        )
        self.wait(2)

        self.play(
            ReplacementTransform(union, diff1),
            TransformMatchingShapes(form_union_group, form_diff1_group)
        )
        self.wait(2)

        self.play(
            ReplacementTransform(diff1, diff2),
            TransformMatchingShapes(form_diff1_group, form_diff2_group)
        )
        self.wait(2)

        self.play(
            ReplacementTransform(diff2, exclusion),
            TransformMatchingShapes(form_diff2_group, form_exclusion_group)
        )
        self.wait(2)
