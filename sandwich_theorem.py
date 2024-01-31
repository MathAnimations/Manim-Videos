from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class SandwichTheorem(Scene):
    def construct(self):
        ax1 = Axes(
            x_range=[-0.8, 0.8],
            y_range=[-0.8, 0.8],
            x_length=7
        ).add_coordinates()
        ax1_labels = ax1.get_axis_labels()

        axes = VGroup(ax1, ax1_labels)

        upper_graph = ax1.plot(lambda x: np.abs(x), x_range=[-0.8, 0.8, 0.001], color=RED)
        lower_graph = ax1.plot(lambda x: -np.abs(x), x_range=[-0.8, 0.8, 0.001], color=BLUE)
        sandwich_graph = ax1.plot(lambda x: x * np.cos(1/x), x_range=[-0.8, 0.8, 0.001], color=GREEN)

        upper_label = ax1.get_graph_label(
            upper_graph, "h(x)", x_val=0.4, direction=UP + LEFT
        )
        lower_label = ax1.get_graph_label(
            lower_graph, "g(x)", x_val=-0.4, direction=UP*1.5
        )
        sandwich_label = ax1.get_graph_label(
            sandwich_graph, "f(x)", x_val=0.2, direction=RIGHT + UP/2
        )

        self.play(
            Create(axes),
            Write(upper_graph),
            Write(upper_label),
            Write(lower_graph),
            Write(lower_label)
        )
        self.play(Write(sandwich_graph), Write(sandwich_label))
        self.wait(2)

        sandwich_group = VGroup(ax1, ax1_labels, upper_graph, lower_graph, sandwich_graph, upper_label, lower_label, sandwich_label)

        self.play(
            sandwich_group.animate.scale(0.5).shift(UP*1.3)
        )
        
        form1 = MathTex(r"g(x)\leq f(x)\leq h(x)").next_to(sandwich_group, DOWN)
        
        self.play(Write(form1))
        self.wait(1)

        ax2 = Axes(
            x_range=[0, 10],
            y_range=[-1, 1],
            x_length=7
        ).add_coordinates()

        dot_u_1 = Dot(point=ax2.c2p(1, 1, 0), color=RED)
        dot_u_2 = Dot(point=ax2.c2p(2, 0.5, 0), color=RED)
        dot_u_3 = Dot(point=ax2.c2p(3, 1/3, 0), color=RED)
        dot_u_4 = Dot(point=ax2.c2p(4, 0.25, 0), color=RED)
        dot_u_5 = Dot(point=ax2.c2p(5, 0.2, 0), color=RED)
        dot_u_6 = Dot(point=ax2.c2p(6, 1/6, 0), color=RED)
        dot_u_7 = Dot(point=ax2.c2p(7, 1/7, 0), color=RED)
        dot_u_8 = Dot(point=ax2.c2p(8, 0.125, 0), color=RED)
        dot_u_9 = Dot(point=ax2.c2p(9, 1/9, 0), color=RED)
        dot_u_10 = Dot(point=ax2.c2p(10, 0.1, 0), color=RED)

        dot_l_1 = Dot(point=ax2.c2p(1, -1, 0), color=BLUE)
        dot_l_2 = Dot(point=ax2.c2p(2, -0.5, 0), color=BLUE)
        dot_l_3 = Dot(point=ax2.c2p(3, -1/3, 0), color=BLUE)
        dot_l_4 = Dot(point=ax2.c2p(4, -0.25, 0), color=BLUE)
        dot_l_5 = Dot(point=ax2.c2p(5, -0.2, 0), color=BLUE)
        dot_l_6 = Dot(point=ax2.c2p(6, -1/6, 0), color=BLUE)
        dot_l_7 = Dot(point=ax2.c2p(7, -1/7, 0), color=BLUE)
        dot_l_8 = Dot(point=ax2.c2p(8, -0.125, 0), color=BLUE)
        dot_l_9 = Dot(point=ax2.c2p(9, -1/9, 0), color=BLUE)
        dot_l_10 = Dot(point=ax2.c2p(10, -0.1, 0), color=BLUE)

        dot_s_1 = Dot(point=ax2.c2p(1, -1, 0), color=GREEN)
        dot_s_2 = Dot(point=ax2.c2p(2, 0.25, 0), color=GREEN)
        dot_s_3 = Dot(point=ax2.c2p(3, -1/9, 0), color=GREEN)
        dot_s_4 = Dot(point=ax2.c2p(4, 1/16, 0), color=GREEN)
        dot_s_5 = Dot(point=ax2.c2p(5, -0.04, 0), color=GREEN)
        dot_s_6 = Dot(point=ax2.c2p(6, 1/36, 0), color=GREEN)
        dot_s_7 = Dot(point=ax2.c2p(7, -1/49, 0), color=GREEN)
        dot_s_8 = Dot(point=ax2.c2p(8, 1/64, 0), color=GREEN)
        dot_s_9 = Dot(point=ax2.c2p(9, -1/81, 0), color=GREEN)
        dot_s_10 = Dot(point=ax2.c2p(10, 0.01, 0), color=GREEN)

        upper_seq = VGroup(dot_u_1, dot_u_2, dot_u_3, dot_u_4, dot_u_5, dot_u_6, dot_u_7, dot_u_8, dot_u_9, dot_u_10)
        lower_seq = VGroup(dot_l_1, dot_l_2, dot_l_3, dot_l_4, dot_l_5, dot_l_6, dot_l_7, dot_l_8, dot_l_9, dot_l_10)
        sandwich_seq = VGroup(dot_s_2, dot_s_3, dot_s_4, dot_s_5, dot_s_6, dot_s_7, dot_s_8, dot_s_9, dot_s_10)

        upper_seq_label = MathTex(r"c_n").set_color(RED)
        upper_seq_label.scale(0.8).shift(UP + RIGHT)

        lower_seq_label = MathTex(r"b_n").set_color(BLUE)
        lower_seq_label.scale(0.8).shift(DOWN + RIGHT)

        sandwich_seq_label = MathTex(r"a_n").set_color(GREEN)
        sandwich_seq_label.scale(0.8).shift(UP/2 + LEFT*3)

        self.play(
            FadeOut(form1),
            ReplacementTransform(sandwich_group, ax2)
        )
        self.play(
            Write(upper_seq),
            Write(lower_seq),
            Write(upper_seq_label),
            Write(lower_seq_label)
        )
        self.play(
            Write(sandwich_seq),
            Write(sandwich_seq_label)
        )
        self.wait(2)

        sandwich_seq_group = VGroup(ax2, upper_seq, lower_seq, sandwich_seq, upper_seq_label, lower_seq_label, sandwich_seq_label)

        self.play(
            sandwich_seq_group.animate.scale(0.5).shift(UP*1.3)
        )

        form2 = MathTex(r"b_n\leq a_n\leq c_n").next_to(sandwich_seq_group, DOWN)
        
        self.play(Write(form2))
        self.wait(1)
