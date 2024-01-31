from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class SqTunnel(ThreeDScene):
    def construct(self):
        self.camera.focal_distance = 200
        sq = Square(color=PURPLE).scale(2).rotate(45*DEGREES)

        self.play(Create(sq))

        for i in range(40):
            sq = sq.copy().rotate(10*DEGREES).scale(.86)
            self.play(FadeIn(sq), run_time=0.05)
        self.play(
            self.camera.theta_tracker.animate.set_value(-3*PI),
            self.camera.zoom_tracker.animate.set_value(300),
            run_time=10
        )
        self.wait(0.5)
