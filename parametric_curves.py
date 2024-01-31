from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class ParametricCurves(Scene):
    def construct(self):
        def f1(t):
            return np.array((np.sin(33 * t)*np.cos(9*t), np.sin(40 * t)*np.sin(7*t), 0))

        def f2(t):
            return np.array((2*np.cos(t) + np.sin(2*t)*np.cos(60*t), np.sin(2 * t) + np.sin(60*t), 0))

        def f3(t):
            return np.array((t - 1.6*np.cos(24*t), t - 1.6*np.sin(25*t), 0))
        
        def f4(t):
            return np.array((-35*np.cos(t) + 65*np.cos(-0.35*t), -35*np.sin(t) - 65*np.sin(-0.35*t), 0))
        
        def f5(t):
            return np.array((3*np.cos(np.cos(7.32*np.round(t)))*1.2*(1+np.cos(16.6*t)), 3*np.sin(16.6*t)**2*np.sin(7.32*t), 0))

        func1 = ParametricFunction(f1, t_range = np.array([0, TAU]), fill_opacity=0).set_color([RED, BLUE])
        func2 = ParametricFunction(f2, t_range = np.array([0, TAU]), fill_opacity=0).set_color([PINK, PURPLE])
        func3 = ParametricFunction(f3, t_range = np.array([0, TAU]), fill_opacity=0).set_color([TEAL, GREEN])
        func4 = ParametricFunction(f4, t_range = np.array([0, 300]), fill_opacity=0).set_color([RED, MAROON])
        func5 = ParametricFunction(f5, t_range = np.array([-10, 10]), fill_opacity=0).set_color([YELLOW, ORANGE])

        func1.scale(3).move_to(ORIGIN)
        func2.scale(1.4).move_to(ORIGIN)
        func3.scale(0.5).shift(3*LEFT + 3*DOWN)
        func4.scale(0.03).move_to(ORIGIN)
        func5.scale(0.7).move_to(ORIGIN)

        self.play(Create(func1), run_time=2.5)
        self.wait(0.5)
        self.play(FadeOut(func1))

        self.play(Create(func2), run_time=2.5)
        self.wait(0.5)
        self.play(FadeOut(func2))

        self.play(Create(func3), run_time=2.5)
        self.wait(0.5)
        self.play(FadeOut(func3))

        self.play(Create(func4), run_time=2.5)
        self.wait(0.5)
        self.play(FadeOut(func4))

        self.play(Create(func5), run_time=2.5)
        self.wait(1)
