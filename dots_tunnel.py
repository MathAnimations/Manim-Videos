from manim import *

class DotsTunnel(MovingCameraScene):
    config.pixel_height = 1920
    config.pixel_width = 1080
    config.frame_height = 16.0
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

    def construct(self):
        self.camera.frame.save_state()
        grid = VGroup(
            *[Dot() for _ in range(100)]
        ).arrange_in_grid(rows=10,cols=10).scale_to_fit_height(4)
        self.play(Create(grid))

        self.play(grid.animate.set_submobject_colors_by_gradient(PURPLE, BLUE))
        self.wait()

        self.play(
            grid.animate.set_height(TAU - MED_SMALL_BUFF),
            self.camera.frame.animate.move_to(ORIGIN).scale(2)
        )
        self.wait()

        self.play(grid.animate.apply_complex_function(np.exp), run_time=5)
        self.play(
            self.camera.frame.animate.move_to(ORIGIN).scale(0.001),
            grid.animate.set_submobject_colors_by_gradient(BLUE, GREEN),
            Rotate(grid, angle=PI/2, about_point=ORIGIN, rate_func=linear),
            run_time=5
        )
