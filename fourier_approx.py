from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class FourierApprox(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-3*PI, 3*PI, 3],
            y_range=[-0.5, 7],
            x_length=7
        ).add_coordinates()
        ax_labels = ax.get_axis_labels()
        axes_group = VGroup(ax, ax_labels)

        g_left = ax.plot(lambda x: x + 3*PI, x_range=[-3*PI, -PI], color=BLUE)
        g_mid = ax.plot(lambda x: x + PI, x_range=[-PI, PI], color=BLUE)
        g_right = ax.plot(lambda x: x - PI, x_range=[PI, 3*PI], color=BLUE)

        approx_1 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 2)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)
        
        approx_2 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 3)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)
        
        approx_3 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 4)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)
        
        approx_4 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 5)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)
        
        approx_5 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 6)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)
        
        approx_6 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 7)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)
        
        approx_7 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 8)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)
        
        approx_8 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 9)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)
        
        approx_9 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 10)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)
        
        approx_10 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 11)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)
        
        approx_11 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 12)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)
        
        approx_12 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 13)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)
        
        approx_13 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 14)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)
        
        approx_14 = ax.plot(lambda x: PI + sum([(2*(-1)**(k+1))/(k) * np.sin(k*x) for k in range(1, 15)]),
                x_range=[-3*PI,3*PI, 0.001],
                use_smoothing=False,
                ).set_color(RED)

        rt = 0.5

        self.play(
            Create(axes_group),
            Write(g_left),
            Write(g_mid),
            Write(g_right),
            Write(approx_1)
        )
        self.wait(rt)
        self.play(ReplacementTransform(approx_1, approx_2), run_time=rt)
        self.play(ReplacementTransform(approx_2, approx_3), run_time=rt)
        self.play(ReplacementTransform(approx_3, approx_4), run_time=rt)
        self.play(ReplacementTransform(approx_4, approx_5), run_time=rt)
        self.play(ReplacementTransform(approx_5, approx_6), run_time=rt)
        self.play(ReplacementTransform(approx_6, approx_7), run_time=rt)
        self.play(ReplacementTransform(approx_7, approx_8), run_time=rt)
        self.play(ReplacementTransform(approx_8, approx_9), run_time=rt)
        self.play(ReplacementTransform(approx_9, approx_10), run_time=rt)
        self.play(ReplacementTransform(approx_10, approx_11), run_time=rt)
        self.play(ReplacementTransform(approx_11, approx_12), run_time=rt)
        self.play(ReplacementTransform(approx_12, approx_13), run_time=rt)
        self.play(ReplacementTransform(approx_13, approx_14), run_time=rt)
        self.wait(1)
