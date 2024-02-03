from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class CircDots(Scene):
    def construct(self):
        self.time=0
        def update_time(dt):
            self.time += dt
        self.add_updater(update_time)

        colors = [
            "#D8BFD8",
            "#DDA0DD",
            "#EE82EE",
            "#DA70D6",
            "#FF00FF",
            "#FF00FF",
            "#BA55D3",
            "#9370DB",
            "#663399",
            "#8A2BE2",
            "#9400D3",
            "#9932CC",
            "#8B008B",
        ]
        cycle_time=2
        rt = 0.3
        dot_radius = 0.25
        total_num = 12
        cur_num = 1

        line = Line(UP*3, DOWN*3).set_stroke(WHITE,4,.5)
        dot = Dot(radius=dot_radius)

        def gen_lines(line_num):
            lines = [
                line.copy().rotate(PI/line_num*i)
                if i < line_num else
                line.copy().set_opacity(0.)
                for i in range(total_num)
            ]
            return VGroup(*lines)

        lines = gen_lines(cur_num)
        
        def get_proportion(i):
            t = self.time%cycle_time + i/cur_num
            p = t if t<=1 else 2-t
            return (1-np.cos(p*PI))/2
        dots = []
        for i in range(total_num):
            dots.append(dot.copy().set_color(colors[i]))
            dots[i]._i = i
            dots[i]._c = colors[i]
            dots[i]._p = get_proportion(i)
            dots[i]._t = 0
        def update_dot(dot, dt):
            dot._t += dt
            dot.move_to(
                lines[dot._i].point_from_proportion(dot._p)
            )
            if dot._i >= cur_num:
                dot.set_opacity(0)
            else:
                dot.set_opacity(1)
                next_p = get_proportion(dot._i)
                if (next_p>=.5 and dot._p<=.5) or (next_p<=.5 and dot._p>=.5) and dot._t>=.5:

                    dot._t = 0
                dot._p = next_p
        for i in range(total_num):
            dots[i].add_updater(update_dot)
            dots[i].update(0)


        t = Tex("$n = 1$", font_size=90)
        t.shift(UP*4)

        self.add(lines, *dots)
        self.play(Write(t))
        self.wait(1.7)

        for i in range(total_num):
            new_lines = gen_lines(i+1)
            t_new = Tex(f"$n = {i+1}$", font_size=90)
            t_new.shift(UP*4)
            self.play(
                ReplacementTransform(lines, new_lines, rate_func=linear, suspend_mobject_updating=False),
                Transform(t, t_new),
                run_time=rt
            )
            cur_num = i+1
            lines = new_lines
            self.wait(0.7)
            
        self.wait(4)
