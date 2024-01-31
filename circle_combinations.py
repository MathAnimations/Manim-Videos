from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

def get_coords(n, r):
    tmp=[]
    for x in range(0,n):
        x_ = (x/n)*360
        tmp.append([(round(math.cos(math.radians(x_)),5))*r,(round(math.sin(math.radians(x_)),5))*r,0])

    return tmp   
radius = 3

class CircleCombinations(Scene):
    def construct(self):
        updater = Tex("$n = 2$", font_size=90)
        updater.shift(UP*4)
        self.add(updater)

        for x in range(2, 15):

            dg = VGroup()

            for a in get_coords(x, radius):
                d = Dot(a, radius=0.1).set_color(PURPLE)
                dg.add(d)

            lg = VGroup()

            for a in range(0,x):
                for b in range(0,x):
                    l = Line(get_coords(x, radius)[a], get_coords(x, radius)[b],stroke_width=1).set_color(PINK)

                    lg.add(l)

            self.play(Create(dg, run_time=0.5, lag_ratio=0.1))
            self.play(Create(lg, run_time=0.7, lag_ratio=0.01))
    
            if x == 14:
                self.play(FadeOut(dg,lg,updater))
            
            else:
                n_t = Tex(f"$n = {x+1}$", font_size=90)
                n_t.shift(UP*4)
                self.play(FadeOut(dg, lg), Transform(updater, n_t), run_time=0.5)

        self.wait()

