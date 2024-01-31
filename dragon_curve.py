from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class Dragon(MovingCameraScene):
    def construct(self):
        dragon_curve = VMobject(stroke_color=BLUE)
        dragon_curve_points = [LEFT, RIGHT]
        dragon_curve.set_points_as_corners(dragon_curve_points)
        dragon_curve.corners = dragon_curve_points
        self.add(dragon_curve)
        self.wait()

        new_points = dragon_curve_points + dragon_curve_points[:-1:-1]
        dragon_curve.set_points_as_corners(new_points)
        dragon_curve.corners = new_points

        def rotate_half_points(points, alpha):
            static_part = points[:len(points)//2]
            about_point = points[len(points)//2]
            mat = rotation_matrix(-PI/2 * alpha, OUT)
            rotated_part = [
                np.dot((point - about_point), mat.T) + about_point
                for point in reversed(static_part)
            ]
            return static_part + [about_point] + rotated_part

        def rotate_half_curve(mobject, alpha):
            corners = mobject.corners
            new_corners = rotate_half_points(corners, alpha)
            mobject.set_points_as_corners(new_corners)
            return mobject

        for it in range(15):
            dragon_curve.set_style(stroke_width=self.camera.frame.width / 10)
            rotated_curve = VMobject().set_points_as_corners(rotate_half_points(dragon_curve.corners, 1))
            self.play(
                UpdateFromAlphaFunc(dragon_curve, rotate_half_curve),
                self.camera.auto_zoom(rotated_curve, margin=1)
            )
            current_corners = rotate_half_points(dragon_curve.corners, 1)
            current_corners = current_corners + current_corners[-1::-1]
            dragon_curve.set_points_as_corners(current_corners)
            dragon_curve.corners = current_corners

        self.wait()

