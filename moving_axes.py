from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class MovingAx(Scene):
    def construct(self):
        xrng = ValueTracker(PI)
        yrng = ValueTracker(2)

        ax = Axes(
            x_range=[-PI, PI, 5],
            y_range=[-2, 2, 5],
            x_length=7
        ).add_coordinates()
        func = VMobject()
        def axUpdater(mobj):
            xmin = -xrng.get_value()
            xmax = +xrng.get_value()
            ymin = -yrng.get_value()
            ymax = +yrng.get_value()
            newax =Axes(x_range=[xmin,xmax, 10],y_range=[ymin,ymax, 10], x_length=7)
            newax.add_coordinates()
            newfunc = newax.plot(
                lambda x: np.sin(x)*x,
                x_range=[xmin,xmax,xrng.get_value()/200],
                use_smoothing=False,
                ).set_color(RED).set_stroke(width=3)
            mobj.become(newax)
            func.become(newfunc)            
        ax.add_updater(axUpdater)

        self.add(ax,func)
        
        
        self.wait(1)
        self.play(
            xrng.animate.set_value(50),
            yrng.animate.set_value(50),
            run_time=15
        )
        self.wait()
